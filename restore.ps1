# Restore script for Enhetsregisteret app
Write-Host "🔄 Restore script for Enhetsregisteret app" -ForegroundColor Green

# Check if backup folder is specified
if ($args.Count -eq 0) {
    Write-Host "❌ Please specify backup folder path" -ForegroundColor Red
    Write-Host "💡 Usage: .\restore.ps1 'path\to\backup\folder'" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "📁 Available backups:" -ForegroundColor Cyan
    
    # Show available backups
    $backups = Get-ChildItem -Path ".." -Directory | Where-Object { $_.Name -like "*enhetsregisteret-app_backup*" }
    if ($backups) {
        foreach ($backup in $backups) {
            Write-Host "   📂 $($backup.Name)" -ForegroundColor White
        }
    } else {
        Write-Host "   No backups found" -ForegroundColor Yellow
    }
    exit 1
}

$backupPath = $args[0]

# Check if backup exists
if (-not (Test-Path $backupPath)) {
    Write-Host "❌ Backup folder not found: $backupPath" -ForegroundColor Red
    exit 1
}

Write-Host "📁 Restoring from: $backupPath" -ForegroundColor Blue
Write-Host "📁 Restoring to: $PWD" -ForegroundColor Blue

# Confirm restore
Write-Host ""
Write-Host "⚠️ This will overwrite all current files!" -ForegroundColor Yellow
$confirm = Read-Host "Are you sure? (y/N)"

if ($confirm -ne "y" -and $confirm -ne "Y") {
    Write-Host "❌ Restore cancelled" -ForegroundColor Red
    exit 0
}

try {
    # Remove current files (except backup and restore scripts)
    $filesToRemove = Get-ChildItem -Path "." -Exclude "backup.ps1", "restore.ps1"
    foreach ($file in $filesToRemove) {
        if ($file.PSIsContainer) {
            Remove-Item -Path $file.FullName -Recurse -Force
        } else {
            Remove-Item -Path $file.FullName -Force
        }
    }
    
    # Copy files from backup
    Copy-Item -Path "$backupPath\*" -Destination "." -Recurse -Force
    
    Write-Host "✅ Restore completed successfully!" -ForegroundColor Green
    Write-Host "🚀 You can now run the app again" -ForegroundColor Cyan
    
} catch {
    Write-Host "❌ Error during restore: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "💡 Try running the RESTORE.ps1 script from the backup folder instead" -ForegroundColor Yellow
}

# Backup script for Enhetsregisteret app
Write-Host "Creating backup of Enhetsregisteret app..." -ForegroundColor Green

# Get current timestamp
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm"
$backupName = "enhetsregisteret-app_backup_$timestamp"

# Create backup folder in parent directory
$backupPath = "..\$backupName"

Write-Host "Creating backup: $backupName" -ForegroundColor Blue

try {
    # Copy all files and folders
    Copy-Item -Path ".\*" -Destination $backupPath -Recurse -Force
    
    if (Test-Path $backupPath) {
        Write-Host "Backup created successfully!" -ForegroundColor Green
        Write-Host "Location: $backupPath" -ForegroundColor Cyan
        
        # Show backup contents
        $fileCount = (Get-ChildItem -Path $backupPath -Recurse -File).Count
        Write-Host "Files backed up: $fileCount" -ForegroundColor Yellow
        
        # Create a restore script in backup folder
        $restoreScript = @"
# Restore script - Run this to restore from backup
Write-Host "Restoring from backup..." -ForegroundColor Green

# Get the original app folder path
`$originalPath = Split-Path (Split-Path `$PSScriptRoot)

Write-Host "Restoring to: `$originalPath" -ForegroundColor Blue

# Copy files back
Copy-Item -Path ".\*" -Destination "`$originalPath" -Recurse -Force

Write-Host "Restore completed!" -ForegroundColor Green
Write-Host "You can now run the app again" -ForegroundColor Cyan
"@
        
        Set-Content -Path "$backupPath\RESTORE.ps1" -Value $restoreScript
        Write-Host "Restore script created: $backupPath\RESTORE.ps1" -ForegroundColor Yellow
        
    } else {
        Write-Host "Backup failed!" -ForegroundColor Red
    }
    
} catch {
    Write-Host "Error creating backup: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
Write-Host "To restore from backup:" -ForegroundColor Cyan
Write-Host "   1. Go to backup folder: $backupPath" -ForegroundColor White
Write-Host "   2. Run: .\RESTORE.ps1" -ForegroundColor White
Write-Host ""

# Also create a zip backup
Write-Host "Creating ZIP backup..." -ForegroundColor Blue
$zipName = "enhetsregisteret-app_backup_$timestamp.zip"
$zipPath = "..\$zipName"

try {
    Compress-Archive -Path ".\*" -DestinationPath $zipPath -Force
    if (Test-Path $zipPath) {
        Write-Host "ZIP backup created: $zipName" -ForegroundColor Green
    }
} catch {
    Write-Host "ZIP backup failed, but folder backup succeeded" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "You now have a safe backup before making changes!" -ForegroundColor Green

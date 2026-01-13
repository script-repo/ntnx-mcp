<#
.SYNOPSIS
    Ralph Wiggum Loop for Amp - Iterative AI development

.DESCRIPTION
    Runs Amp in a loop, feeding it the same prompt repeatedly until completion.
    Each iteration sees its previous work in files and git history.

.PARAMETER Prompt
    The task description for Amp to work on

.PARAMETER MaxIterations
    Maximum number of iterations (default: 50, use 0 for unlimited)

.PARAMETER CompletionMarker
    Text that signals completion (checked in Amp's output)

.EXAMPLE
    .\ralph-loop.ps1 -Prompt "Build a REST API with CRUD operations" -MaxIterations 20 -CompletionMarker "COMPLETE"

.EXAMPLE
    .\ralph-loop.ps1 "Fix all failing tests" -MaxIterations 30
#>

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$Prompt,

    [Parameter()]
    [int]$MaxIterations = 50,

    [Parameter()]
    [string]$CompletionMarker = ""
)

$iteration = 0

Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "🔄 Starting Ralph Wiggum Loop" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""
Write-Host "Prompt: $Prompt" -ForegroundColor Yellow
Write-Host "Max Iterations: $(if ($MaxIterations -eq 0) { 'Unlimited' } else { $MaxIterations })" -ForegroundColor Yellow
if ($CompletionMarker) {
    Write-Host "Completion Marker: $CompletionMarker" -ForegroundColor Yellow
}
Write-Host ""
Write-Host "Press Ctrl+C to stop manually" -ForegroundColor Gray
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Build the full prompt with iteration context
$basePrompt = @"
$Prompt

---
RALPH LOOP INSTRUCTIONS:
- This is iteration {ITERATION} of the Ralph loop
- Review your previous work in files and git history
- Continue iterating until the task is fully complete
- Run all validation commands (tests, builds, linters)
- Fix any issues you find
$(if ($CompletionMarker) { "- When COMPLETELY done, output: $CompletionMarker" })
"@

while ($true) {
    $iteration++
    
    # Check max iterations
    if ($MaxIterations -gt 0 -and $iteration -gt $MaxIterations) {
        Write-Host ""
        Write-Host "🛑 Max iterations ($MaxIterations) reached. Stopping." -ForegroundColor Red
        break
    }

    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
    Write-Host "🔄 Ralph Iteration $iteration" -ForegroundColor Cyan
    Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
    Write-Host ""

    # Replace iteration placeholder
    $currentPrompt = $basePrompt -replace '\{ITERATION\}', $iteration

    # Run Amp and capture output
    $output = & amp -p $currentPrompt --dangerously-skip-permissions 2>&1 | Tee-Object -Variable ampOutput
    $outputText = $ampOutput -join "`n"

    # Check for completion marker
    if ($CompletionMarker -and $outputText -match [regex]::Escape($CompletionMarker)) {
        Write-Host ""
        Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Green
        Write-Host "✅ Completion marker detected: $CompletionMarker" -ForegroundColor Green
        Write-Host "   Finished after $iteration iterations" -ForegroundColor Green
        Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Green
        break
    }

    # Brief pause between iterations
    Start-Sleep -Seconds 2
}

Write-Host ""
Write-Host "Ralph loop ended." -ForegroundColor Cyan

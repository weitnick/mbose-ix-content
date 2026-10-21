# Open each .docx in Word (read-only), report its page count, and optionally export a PDF next to it.
# Usage: powershell -NoProfile -File word_check.ps1 [-Pdf] <file1.docx> [<file2.docx> ...]
param([switch]$Pdf, [Parameter(ValueFromRemainingArguments = $true)][string[]]$Files)
$w = New-Object -ComObject Word.Application
$w.Visible = $false
$w.DisplayAlerts = 0
try {
    foreach ($f in $Files) {
        $full = (Resolve-Path $f).Path
        $d = $w.Documents.Open($full, $false, $true)
        "{0}: {1} pages, {2} equations" -f (Split-Path $full -Leaf), $d.ComputeStatistics(2), $d.OMaths.Count
        if ($Pdf) { $d.ExportAsFixedFormat(($full -replace '\.docx$', '.pdf'), 17) }
        $d.Close($false)
    }
}
finally { $w.Quit() }

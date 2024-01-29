%! Class = CLASS_NAME
%! Author = ibw
%! Date = 09.11.23

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{grathesis}[2023/09/23 v0.1 Klasse fuer Michael Graber Thesen]
\LoadClass[11pt,a4paper,bibliography=totoc,listof=totoc]{scrreprt}
\ProcessOptions\relax

\RequirePackage[T1]{fontenc}
\RequirePackage{graphicx}
\RequirePackage{varwidth}

\RequirePackage{setspace}
\onehalfspacing

\RequirePackage[left=3cm, right=3cm]{geometry}


\RequirePackage{helvet}
\renewcommand{\familydefault}{\sfdefault}

\RequirePackage[english,ngerman]{babel}

\RequirePackage{layout}

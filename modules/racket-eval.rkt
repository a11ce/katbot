#lang racket
(require racket/sandbox)

(define prog
  (call-with-input-file "modules/racket-eval/in.rkt"
                        (lambda (in) (port->list read in))))
;(define prog (file->list "racket-eval/in.rkt" read-syntax))
(displayln prog)
(define out-port
  (open-output-file "modules/racket-eval/out.txt" #:exists 'replace))
(define err-port
  (open-output-file "modules/racket-eval/err.txt" #:exists 'replace))

(parameterize ([current-output-port out-port] [current-error-port err-port])
  (define evaler (make-evaluator 'racket))

  (for ([exp prog])
    (displayln (evaler exp)))

  (close-output-port out-port)
  (close-output-port err-port))

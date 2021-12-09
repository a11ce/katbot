#lang racket
(require racket/sandbox)

(define prog (file->list "modules/racket-eval/in.rkt"))

(define out-port (open-output-file "modules/racket-eval/out.txt"
                                   #:exists 'replace))
(define evaler
  (parameterize
      ([sandbox-output out-port])
    (make-evaluator 'racket)))

(for ([exp prog])
  (evaler exp))

(close-output-port out-port)

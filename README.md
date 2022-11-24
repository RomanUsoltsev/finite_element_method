# finite_element_method
numerical solution of a differential equation by the finite element method

${\displaystyle \frac{d}{dx}(C(x)\cdot \frac{du}{dx}}) = f(x)$

${\displaystyle u(0) = 0 }$

${\displaystyle \frac{du}{dx} (L) =  \frac{-P}{E \cdot A(L)} }$

---

${\displaystyle   C(x) = E \cdot A(x)}$

${\displaystyle   C(x) = E \cdot  b \cdot ( 0.1 + \frac{x}{10 \cdot L})}$

${\displaystyle A(x) = b \cdot h(x) }$

${\displaystyle h(x) = 0.1 + \frac{x}{10 \cdot L} }$

${\displaystyle f(x) = p \cdot g \cdot A(x) }$

---

${\displaystyle L = 5 \, м }$

${\displaystyle p = 2150 \, \frac{кг}{м^3} }$

${\displaystyle g = 9.81 \, \frac{м}{с^2} }$

${\displaystyle P = 30000 \, Н }$

${\displaystyle E = 3000 \, Па }$

${\displaystyle b = 0.1 \, м }$

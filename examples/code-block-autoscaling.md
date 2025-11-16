---
theme: default
---

# Code Block Auto-Scaling

This demonstrates how code blocks are automatically scaled to fit the slide.

---

## Traditional Rendering (Without Auto-Scaling)

Long lines would stick out from the slide edge:

```javascript
const veryLongFunctionName = (parameterOne, parameterTwo, parameterThree, parameterFour) => {
  return someReallyLongExpressionThatWouldNormallyOverflowTheSlideWidth(parameterOne, parameterTwo, parameterThree, parameterFour);
}
```

---

## Auto-Scaling (Enabled)

With auto-scaling, the code block shrinks to fit:

```javascript
const veryLongFunctionName = (parameterOne, parameterTwo, parameterThree, parameterFour) => {
  return someReallyLongExpressionThatWouldNormallyOverflowTheSlideWidth(parameterOne, parameterTwo, parameterThree, parameterFour);
}

const anotherLongFunction = () => console.log('This is a very long line that would normally extend beyond the slide boundaries');
```

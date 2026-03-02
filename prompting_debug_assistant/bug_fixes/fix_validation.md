## Bug 1 – bug1_fixed.py
- **Input**: items=[1,2,3,4,5], n=3  
- **Expected Output**: [3,4,5]  
- **Actual Output**: [3,4,5] ✅

## Bug 2 – bug2_fixed.js
- **Input**: [3,1,2,3,2,4,1]  
- **Expected Output**: [1,2,3,4]  
- **Actual Output**: Not executed (JavaScript runtime not available in this environment). ⚠️

## Bug 3 – bug3_fixed.java
- **Input**: ["hi", null, "world"]  
- **Expected Output**: 3.5  
- **Actual Output**: Not executed (JDK not available in this environment). ⚠️

## Bug 4 – bug4_fixed.py
- **Input**: {"apples":"10","oranges":"5","pears":"2"}  
- **Expected Output**: 17  
- **Actual Output**: 17 ✅

## Bug 5 – bug5_fixed.js
- **Input**: userId=42 with mocked fetch returning `{ name: "Ada Lovelace" }`  
- **Expected Output**: "ADA LOVELACE"  
- **Actual Output**: Not executed (JavaScript runtime not available in this environment). ⚠️

## Bug 6 – bug6_fixed.py
- **Input**: nums=[1,2,4,3], target=7  
- **Expected Output**: (4,3)  
- **Actual Output**: (4,3) ✅

## Additional Python edge tests (passed)
- **Bug 1**: items=[1,2,3], n=3 -> [1,2,3] ✅  
- **Bug 1**: items=[1,2,3], n=0 -> [] ✅  
- **Bug 6**: nums=[1,2,4,8], target=7 -> None ✅

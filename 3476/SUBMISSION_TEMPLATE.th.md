# บันทึกการแก้โจทย์

ไฟล์นี้ต้องเขียนโดยนักศึกษาด้วยคำพูดของตนเอง

ใช้ template นี้เฉพาะกับโจทย์ OJ ที่ถูกระบุว่าต้องส่ง learning log เท่านั้น

ห้ามให้ AI เขียนไฟล์นี้แทนคุณ AI อาจช่วยตรวจ grammar, formatting หรือความชัดเจนได้ หลังจากที่คุณเขียนเนื้อหาของตนเองแล้ว

ถ้าใช้ AI กับโจทย์ learning-log-required นี้ ต้องทำไฟล์ `ai_reflection.md` ด้วย

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
3394
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
683238
```

สถานะ OJ:

```text
Pass
```

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

```text
0-15 minutes
```

เลือกหนึ่งข้อ:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```

วิธีนับเวลา:

- นับเฉพาะเวลาที่ตั้งใจทำโจทย์นี้ด้วยตนเองจริง ๆ
- เริ่มนับตั้งแต่ตอนที่อ่านโจทย์ครั้งแรก
- ไม่นับเวลาพัก กินข้าว เรียน นอน เวลาที่ทำโจทย์อื่น หรือเวลาที่ไม่ได้ทำโจทย์นี้
- ถ้าใช้ AI ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อน prompt แรกที่ถาม AI
- ถ้าถามเพื่อน TA หรือผู้สอน ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อนขอความช่วยเหลือครั้งแรก
- ถ้าใช้ทั้ง AI และความช่วยเหลือจากคน ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อนขอความช่วยเหลือจากภายนอกครั้งแรก ไม่ว่าจะเป็น AI หรือคน
- ถ้าไม่ได้ใช้ AI และไม่ได้ขอความช่วยเหลือจากคน ให้นับเวลาถึงก่อนเขียน `submission.md`
- ประมาณเวลาได้ แต่ต้องซื่อสัตย์

---

## 2. ความเข้าใจโจทย์ของฉัน

เขียนโจทย์ด้วยคำพูดของตนเอง

ให้อธิบาย input, output และ constraints สำคัญด้วย

ถ้ายังไม่เข้าใจโจทย์ทั้งหมด ให้เขียนสิ่งที่เข้าใจในตอนนี้ ความเข้าใจอาจยังไม่ครบหรืออาจผิดได้ แต่ต้องพยายามอธิบายอย่างจริงใจ

```text
โจทย์นี้ให้รับข้อมูลชื่อกับรหัสของแมวและสุนัขจิ้งจอก แล้วแยกออกเป็น 2 กลุ่ม โดยถ้าไม่มี Cat01 หรือ Fox01 ก็จะเพิ่ม Garfield หรือ Fubuki ให้ตามเงื่อนไข จากนั้นนับจำนวนและเรียงข้อมูลตามเลขรหัสจากน้อยไปมาก

Input
รับจำนวนข้อมูล n แล้วรับข้อมูลชื่อกับรหัสทีละบรรทัด เช่น {"Milo": "Cat02"}
Output
แสดงจำนวนแมว (Cat) และสุนัขจิ้งจอก (Fox) แล้วแสดงชื่อกับรหัสของแต่ละกลุ่ม โดยเรียงตามเลขในรหัสจากน้อยไปมาก

ใช้ dictionary เก็บชื่อกับรหัส และใช้ startswith() แยกกลุ่มตามรหัส เช่น Cat01 หรือ Fox02 ส่วน sorted() ใช้เรียงลำดับตามตัวเลขในรหัส ไม่ใช่ตามชื่อสัตว์
```

---

## 3. แผนแรกของฉัน

เขียนแผนแรกก่อนรับความช่วยเหลือจาก AI เพื่อน TA ผู้สอน หรือก่อนสรุป code สุดท้าย

ถ้าใช้ AI ให้เขียนแผนที่มีอยู่ก่อน prompt แรกที่ถาม AI

ถ้าถามเพื่อน TA หรือผู้สอน ให้เขียนแผนที่มีอยู่ก่อนถาม

ถ้าไม่ได้ใช้ AI และไม่ได้ขอความช่วยเหลือจากคน ให้เขียนแผนที่มีอยู่ก่อนหรือระหว่างเริ่มเขียน code

แผนนี้เขียนแบบคร่าว ๆ ได้ อาจยังไม่สมบูรณ์หรืออาจต่างจากวิธีสุดท้าย

สามารถเขียนเป็น pseudocode, flowchart idea หรือขั้นตอนความคิดได้

```text
Step 1: 
รับข้อมูลชื่อและรหัส
n = int(input())
group = {}
for _ in range(n):
    line = input().strip().strip("{}")
    k, v = line.split(":")
    k = k.strip().strip('"').strip("'")
    v = v.strip().strip('"').strip("'")
    group[k] = v

รับข้อมูลทั้งหมด n บรรทัด แล้วแยกชื่อกับรหัสออกจากกัน โดยเก็บไว้ใน dictionary ชื่อ group เช่น {"Milo": "Cat02"} จะได้ชื่อ Milo และรหัส Cat02

Step 2:
เพิ่มข้อมูลเริ่มต้นและแยกกลุ่ม
if "Cat01" not in group.values() and "Garfield" not in group:
    group["Garfield"] = "Cat01"
if "Fox01" not in group.values() and "Fubuki" not in group:
    group["Fubuki"] = "Fox01"

cats = {name: code for name, code in group.items() if code.startswith("Cat")}
foxes = {name: code for name, code in group.items() if code.startswith("Fox")}

ถ้าไม่มีทั้งรหัส Cat01 และชื่อ Garfield จะเพิ่ม Garfield เข้าไป เช่นเดียวกับ Fox01 และ Fubuki จากนั้นใช้ startswith() แยกข้อมูลเป็นกลุ่มแมว cats และกลุ่มสุนัขจิ้งจอก foxes

Step 3: 
นับจำนวนและเรียงตามรหัส
print(f"Cat : {len(cats)}")
print(f"Fox : {len(foxes)}")
for name in sorted(cats, key=lambda nm: int("".join(ch for ch in cats[nm] if ch.isdigit()))):
    print(f"{name} : {cats[name]}")
for name in sorted(foxes, key=lambda nm: int("".join(ch for ch in foxes[nm] if ch.isdigit()))):
    print(f"{name} : {foxes[name]}")

ใช้ len() นับจำนวนสัตว์แต่ละกลุ่ม แล้วใช้ sorted() เรียงตามตัวเลขในรหัสจากน้อยไปมาก โดย isdigit() ช่วยเลือกเฉพาะตัวเลข เช่น Cat12 จะได้เลข 12 สุดท้ายพิมพ์ชื่อและรหัสออกมาตามลำดับที่เรียงไว้
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

อธิบายสั้น ๆ ว่า algorithm หรือวิธีสุดท้ายที่ใช้จริงใน code ที่ส่งคืออะไร

หัวข้อนี้ต่างจาก Section 3:

- Section 3 คือแผนแรกก่อนใช้ AI ก่อนรับความช่วยเหลือจากคน หรือก่อนเขียน code สุดท้าย
- Section 4 คือวิธีสุดท้ายที่ใช้ใน solution จริง
- ถ้าวิธีสุดท้ายเหมือนกับแผนแรก ให้เขียนว่าเหมือนกัน และอธิบายสั้น ๆ ว่าทำไม

ห้ามคัดลอกคำอธิบายจาก AI

ห้ามคัดลอกคำอธิบายจากคนอื่น

```text
เหมือนกันกับวิธีคิดแรก เนื่องจากส่งแล้วผ่าน
```

---

## 5. การทดสอบของฉัน

เขียน test cases อย่างน้อย 3 กรณีที่ลองเองหรือออกแบบเอง

พยายามเลือก test cases ที่แตกต่างกัน

แต่ละ test case ให้อธิบายว่าทำไมเลือกกรณีนั้น

ถ้า input หรือ output มีหลายบรรทัด ให้เขียนไว้ใน text blocks

### Test Case 1

ทำไมเลือก case นี้:

```text
ทดสอบกรณีที่มี Cat01 อยู่แล้ว แต่ชื่อไม่ใช่ Garfield โปรแกรมจะไม่เพิ่ม Garfield และจะเพิ่ม Fubuki เพราะยังไม่มี Fox01 เพื่อให้เห็นว่าเงื่อนไขการเพิ่มข้อมูลของแต่ละกลุ่มทำงานแยกกัน
```

Input:

```text
3
{"Luna": "Cat01"}
{"Pip": "Cat02"}
{"Mika": "Fox04"}
```

Expected output:

```text
Cat : 2
Fox : 2
Luna : Cat01
Pip : Cat02
Fubuki : Fox01
Mika : Fox04
```

Actual output:

```text
Cat : 2
Fox : 2
Luna : Cat01
Pip : Cat02
Fubuki : Fox01
Mika : Fox04
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
ทดสอบเงื่อนไขที่ชื่อ Garfield และ Fubuki มีอยู่แล้ว แม้จะไม่มีรหัส Cat01 หรือ Fox01 โปรแกรมก็จะไม่เพิ่มข้อมูลใหม่ เพราะโค้ดเช็กทั้งรหัสและชื่อก่อนเพิ่ม
```

Input:

```text
4
{"Garfield": "Cat05"}
{"Tama": "Cat02"}
{"Fubuki": "Fox06"}
{"Kuro": "Fox03"}
```

Expected output:

```text
Cat : 2
Fox : 2
Tama : Cat02
Garfield : Cat05
Kuro : Fox03
Fubuki : Fox06
```

Actual output:

```text
Cat : 2
Fox : 2
Tama : Cat02
Garfield : Cat05
Kuro : Fox03
Fubuki : Fox06
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
ทดสอบกรณีที่ยังไม่มี Cat01 โปรแกรมจึงเพิ่ม Garfield แต่มี Fox01 อยู่แล้วจึงไม่เพิ่ม Fubuki ซ้ำ อีกทั้งยังตรวจสอบว่ารหัสเรียงตามตัวเลขจากน้อยไปมาก เช่น Cat03 ต้องมาก่อน Cat11
```

Input:

```text
4
{"Mimi": "Cat11"}
{"Rin": "Cat03"}
{"Nana": "Fox10"}
{"Fubuki": "Fox01"}
```

Expected output:

```text
Cat : 3
Fox : 2
Garfield : Cat01
Rin : Cat03
Mimi : Cat11
Fubuki : Fox01
Nana : Fox10
```

Actual output:

```text
Cat : 3
Fox : 2
Garfield : Cat01
Rin : Cat03
Mimi : Cat11
Fubuki : Fox01
Nana : Fox10
```

Result:

```text
Pass
```

---

## 6. การใช้ AI

ใช้ AI กับโจทย์นี้หรือไม่

```text
No
```

ถ้าใช้ AI ต้องทำไฟล์นี้ด้วย:

```text
ai_reflection.md
```

ถ้าถามเฉพาะเพื่อน TA หรือผู้สอน และไม่ได้ใช้ AI ไม่ต้องทำ `ai_reflection.md`

---

## 7. ความช่วยเหลือจากคน / การร่วมมือ

ได้ถามเพื่อน TA ผู้สอน หรือบุคคลอื่นเพื่อขอความช่วยเหลือในโจทย์นี้หรือไม่

```text
No
```

ถ้าใช่ ให้อธิบายสั้น ๆ ว่าได้รับความช่วยเหลือแบบใด

ตัวอย่างที่อนุญาต:

- อธิบายความหมายของโจทย์
- อธิบาย concept การเขียนโปรแกรม
- ให้ hint เกี่ยวกับแนวทาง
- คุยเรื่อง debugging
- คุยเรื่อง test cases
- ช่วยอธิบาย error message

สิ่งที่ไม่อนุญาต:

- คัดลอก code ของผู้อื่น
- ส่ง solution ของผู้อื่น
- ขอให้ผู้อื่นเขียน solution ให้
- ใช้ OJ submission ของผู้อื่น
- ขอให้ผู้อื่นส่ง OJ แทน

ใครช่วยคุณ

```text

```

เขาช่วยอะไร

```text

```

คุณยังทำอะไรด้วยตนเอง

```text

```

คุณคัดลอก code จากคนอื่นหรือไม่

```text
No
```

---

## 8. คำรับรองของนักศึกษา

เขียน `Yes` ในแต่ละ statement

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. |Yes|
| I understand my final code. |Yes|
| I recorded the real OJ status. |Yes|
| I did not copy AI-generated text directly into this file. |Yes|
| I did not copy code from another person. |Yes|
| If I received human help, I disclosed it in this file. |Yes|
| I submitted the final code to the OJ by myself. |Yes|

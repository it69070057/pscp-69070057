# บันทึกการแก้โจทย์

ไฟล์นี้ต้องเขียนโดยนักศึกษาด้วยคำพูดของตนเอง

ใช้ template นี้เฉพาะกับโจทย์ OJ ที่ถูกระบุว่าต้องส่ง learning log เท่านั้น

ห้ามให้ AI เขียนไฟล์นี้แทนคุณ AI อาจช่วยตรวจ grammar, formatting หรือความชัดเจนได้ หลังจากที่คุณเขียนเนื้อหาของตนเองแล้ว

ถ้าใช้ AI กับโจทย์ learning-log-required นี้ ต้องทำไฟล์ `ai_reflection.md` ด้วย

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
3537
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
693407
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
Input
ใส่รายชื่อผู้เล่นทีละบรรทัด รูปแบบ {ชื่อ:บทบาท} เช่น {Red:Crewmate} พิมพ์ Start เมื่อใส่ครบ
ใส่ชื่อคนที่ถูกโหวตออกทีละบรรทัด พิมพ์ End เมื่อจบ

Output
จำนวน Impostor ที่ยังเหลือ เช่น 1 Impostor Remains
รายชื่อคนที่ยังรอด (***Alive***) เรียงตามตัวอักษร รูปแบบ ชื่อ : บทบาท
รายชื่อคนที่ถูกโหวตออก (***Dead***) เรียงตามตัวอักษร

ชื่อห้ามซ้ำกัน และห้ามมี : ในชื่อ
ต้องสะกด Impostor ให้ตรง (ตัว I ใหญ่) ไม่งั้นไม่ถูกนับ
Start และ End ต้องพิมพ์ให้ตรงตัวอักษร ไม่งั้นโปรแกรมจะรอรับข้อมูลต่อไปเรื่อยๆ
ชื่อที่ไม่มีในรายชื่อ หรือถูกโหวตไปแล้ว จะถูกข้ามไป ไม่ error
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
โปรแกรมวนอ่านทีละบรรทัดจนเจอคำว่า Start แต่ละบรรทัดจะตัด { } และเครื่องหมายคำพูดออก แล้วแยกด้วย : เป็นชื่อกับบทบาท เก็บลง dict alive เช่น alive["Red"] = "Crewmate"

Step 2:
โปรแกรมวนอ่านชื่อทีละบรรทัดจนเจอคำว่า End ถ้าชื่อนั้นอยู่ใน alive จะดึงออกด้วย pop แล้วย้ายไปเก็บใน dead พร้อมบทบาทเดิม ถ้าไม่มีชื่อนี้ก็ข้ามไป

Step 3: 
วนดู alive เพื่อนับว่ามี Impostor เหลือกี่คน แล้วพิมพ์

<จำนวน> Impostor Remains
***Alive*** ตามด้วยรายชื่อคนที่รอด เรียงตามตัวอักษร
***Dead*** ตามด้วยรายชื่อคนที่ถูกโหวตออก เรียงตามตัวอักษร
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
ทดสอบโดยเลือกโหวตออก Impostor เพียงคนเดียวจากสองคน เพื่อเช็กว่า
การนับ Impostor ที่เหลือ1คน ถูกต้องมั้ย
บทบาทเปลี่ยนเป็น dead พร้อมกับชื่อ (Black : Impostor)
การเรียงชื่อในฝั่ง Alive
```

Input:

```text
{Pink:Crewmate}
{Black:Impostor}
{White:Crewmate}
{Cyan:Impostor}
Start
Black
End
```

Expected output:

```text
1 Impostor Remains
***Alive***
Cyan : Impostor
Pink : Crewmate
White : Crewmate
***Dead***
Black : Impostor
```

Actual output:

```text
1 Impostor Remains
***Alive***
Cyan : Impostor
Pink : Crewmate
White : Crewmate
***Dead***
Black : Impostor
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
ไม่มีใครถูกโหวตออก พิมพ์ End ทันที เพื่อเช็กว่าฝั่ง Dead ว่างได้โดยไม่ error และคนทั้งหมดยังอยู่ใน Alive
```

Input:

```text
{"Lime":"Impostor"}
{'Orange':'Crewmate'}
{ Yellow : Crewmate }
Start
End
```

Expected output:

```text
1 Impostor Remains
***Alive***
Lime : Impostor
Orange : Crewmate
Yellow : Crewmate
***Dead***
```

Actual output:

```text
1 Impostor Remains
***Alive***
Lime : Impostor
Orange : Crewmate
Yellow : Crewmate
***Dead***
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
โหวต Impostor ออกหมดแล้ว + ชื่อที่ไม่มีในเกมและโหวตซ้ำ ทดสอบความทนทานของโปรแกรมต่ออินพุตที่ไม่ปกติ

- Impostor เหลือ 0 เพื่อเช็กว่าตัวนับแสดง 0 Impostor Remains ได้ 
เช็กชื่อสีที่ไม่มีในเกม(Ghost)เพื่อเช็กว่าโปรแกรมข้ามไปเฉยๆ ไม่ error (เพราะมีเงื่อนไข if name in alive)

- โหวตซ้ำคนเดิม (Banana สองครั้ง) เพื่อเช็กว่าครั้งที่สองไม่มีผล และ Banana ไม่ถูกบันทึกซ้ำใน Dead
เรียงชื่อฝั่ง Dead (Banana ถูกโหวตก่อน Brown แต่แสดงผลเรียงตามตัวอักษร) เพื่อเช็กว่าการเรียงไม่ขึ้นกับลำดับที่โหวต
```

Input:

```text
{Brown:Impostor}
{Purple:Crewmate}
{Banana:Impostor}
Start
Banana
Ghost
Brown
Banana
End
```

Expected output:

```text
0 Impostor Remains
***Alive***
Purple : Crewmate
***Dead***
Banana : Impostor
Brown : Impostor
```

Actual output:

```text
0 Impostor Remains
***Alive***
Purple : Crewmate
***Dead***
Banana : Impostor
Brown : Impostor
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

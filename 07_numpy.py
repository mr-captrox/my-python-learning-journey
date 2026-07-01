# ============================================================
#   🔢  NUMPY — Basics & Image Processing
# ============================================================
#   Author  : Md Sourav Oyaj
#   Install : pip install numpy  (inside your venv)
#   Prerequisite: 01_python_basics.py
# ============================================================
#   HOW TO USE:
#   ▸ Open in VSCode → right-click → "Run in Interactive Window"
#   ▸ Each # %% block is one runnable cell (Shift+Enter)
#
#   📝 Same variable names across cells are fine here.
#      The Interactive Window keeps ONE shared memory (kernel).
#      Re-using 'arr' in a new cell just overwrites the old value.
#      This is normal and expected in notebook-style learning.
# ============================================================

# %%
import numpy as np
print("NumPy version:", np.__version__)


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  PART 1 — NUMPY BASICS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# %%
# ── 1.1 Array Creation & Attributes ──────────────
# ndarray = N-Dimensional Array. Unlike Python lists, all
# elements must be the SAME type — this enables fast math.

arr = np.array([1, 2, 3, 4])               # 1D
print(arr, type(arr))                       # [1 2 3 4]  <class 'numpy.ndarray'>

arr = np.array([[1, 2, 3, 4],              # 2D — 2 rows × 4 cols
                [5, 6, 7, 8]])
print(arr.ndim, arr.shape)                  # 2  (2, 4)

arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],    # 3D
                [[9,10,11,12],[13,14,15,16]],       # Shape = (Blocks, Rows, Cols)
                [[9,10,11,12],[13,14,15,16]]])
print(arr.ndim, arr.shape)                  # 3  (3, 2, 4)

# ndmin → force a minimum number of dimensions
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)          # [[[[[1 2 3 4]]]]]
print(arr.shape)    # (1, 1, 1, 1, 4)

# ✅ TASK: Create a 3D array of shape (2, 3, 4). Print ndim and shape.


# %%
# ── 1.2 Indexing ──────────────────────────────────
# arr[row, col]  for 2D  |  arr[block, row, col]  for 3D
# Negative index counts from the end:  -1 = last element.

arr = np.array([[1, 2, 3, 4],
                [1, 2, 3, 4]])
print(arr[1, 1])    # 2  — row 1, col 1

arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])
print(arr[1, -1])   # 10  — last element of row 1

arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],
                [[9,10,11,12],[13,14,15,16]]])
print(arr[1, 1, 1]) # 14  — block 1, row 1, col 1

# ✅ TASK: Access the TOP-LEFT and BOTTOM-RIGHT elements of a 3×3 array.


# %%
# ── 1.3 Slicing ───────────────────────────────────
# arr[start:stop:step]  →  stop is NOT included
# Works on each axis independently for 2D: arr[row_slice, col_slice]

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[0:3])       # [1 2 3]
print(arr[-9:-1])     # [1 2 3 4 5 6 7 8]  — negative range
print(arr[0:5:2])     # [1 3 5]  — every 2nd element
print(arr[1::2])      # [2 4 6 8]

arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])
print(arr[0, 0:])     # [1 2 3 4 5]  — all cols of row 0
print(arr[1, 2::2])   # [8 10]  — col 2 and 4 of row 1
print(arr[0:2, 2])    # [3 8]   — col 2 of BOTH rows
print(arr[0:2, 1:-1]) # [[2 3 4]   — rows 0-1, cols 1 to second-last
                       #  [7 8 9]]

# ✅ TASK: From a 2×5 array, extract the last 2 columns of both rows.


# %%
# ── 1.4 Data Types & astype() ────────────────────
# NumPy stores all elements as the SAME type.
# dtype='i4'  = int32  |  'f' = float32  |  'U6' = unicode string
# astype() converts without changing the original array.

arr = np.array([1, 2, 3, 4, 5], dtype='i4')  # force int32
print(arr.dtype)       # int32

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)       # <U6  — unicode string, max 6 chars

arr = np.array([1, 2, 3, 4, 0], dtype='i4')

newarr = arr.astype('f')        # int → float32
print(newarr)                   # [1. 2. 3. 4. 0.]
print(newarr.dtype)             # float32

boolarray = arr.astype(bool)    # 0 → False, anything else → True
print(boolarray)                # [ True  True  True  True False]

# ✅ TASK: Create an int array and convert to float. Then convert back to bool.


# %%
# ── 1.5 Copy vs View ──────────────────────────────
# copy()  → owns its data. Changes do NOT affect the original.
# view()  → shares data.  Changes DO  affect the original.
# .base   → None if owns data (copy)  |  original array if view

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)   # [42  2  3  4  5]
print(x)     # [ 1  2  3  4  5]  ← copy — unaffected

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)   # [42  2  3  4  5]
print(x)     # [42  2  3  4  5]  ← view — mirrors arr!

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)   # [31  2  3  4  5]  ← original changed via view!

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)    # None       ← owns data
print(y.base)    # [1 2 3 4 5] ← points to arr

# ✅ TASK: Prove arr[1:3] is a view — change the slice and check if arr changes.


# %%
# ── 1.6 Reshape ───────────────────────────────────
# reshape() changes shape WITHOUT changing the data.
# Total elements must stay the same.
# -1  tells NumPy: "calculate this dimension for me."
# reshape() usually returns a VIEW (.base prints the original).

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

narr    = arr.reshape(-1)          # same as flatten to 1D
newarr  = arr.reshape(4, 3)        # 4 rows × 3 cols
print(newarr)
print(newarr.reshape(-1))          # flatten back to 1D

threedarr = arr.reshape(2, 2, 3)   # 3D
print(threedarr)
print(threedarr.base)              # prints arr  → it's a VIEW

newarr1 = arr.reshape(2, 1, -1)    # NumPy calculates last dim → (2,1,6)
print(newarr1.shape)

# ✅ TASK: Reshape np.arange(1, 25) to (2, 3, 4). Print shape. Then flatten it.


# %%
# ── 1.7 Iteration ─────────────────────────────────
# for loop  → iterates the FIRST axis (rows for 2D)
# nditer    → visits EVERY element regardless of shape (flattened order)
# ndenumerate → like enumerate() — gives index tuple + value

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y, end=" ")     # 1 2 3 4 5 6
print()

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z, end=" ")
print()

for x in np.nditer(arr):
    print(x, end=" ")        # same output, cleaner
print()

# nditer with type conversion during iteration
for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
    print(x, end=" ")        # converts to byte-string on the fly
print()

# nditer on a slice: only iterate specific rows/cols
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[1:, ::2]):   # row 1 onward, every 2nd col
    print(x, end=" ")               # 5 7
print()

# ndenumerate: get index + value
for idx, x in np.ndenumerate(arr):
    print(idx, x)    # (0,0) 1 | (0,1) 2 | ...

# ✅ TASK: Use ndenumerate on a 3×3 array. Print only elements at even-index rows.


# %%
# ── 1.8 Joining Arrays ────────────────────────────
# concatenate → join along an EXISTING axis  (no new axis)
# stack       → join along a NEW axis        (adds a dimension)
# hstack      → side by side (horizontal)
# vstack      → top and bottom (vertical)
# dstack      → depth-wise (adds a 3rd axis)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(np.concatenate((arr1, arr2)))        # [1 2 3 4 5 6]

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.concatenate((a, b), axis=1))     # join on columns

print(np.stack((arr1, arr2), axis=1))     # [[1 4][2 5][3 6]] — new axis
print(np.hstack((arr1, arr2)))            # [1 2 3 4 5 6]
print(np.vstack((arr1, arr2)))            # [[1 2 3][4 5 6]]
print(np.dstack((arr1, arr2)))            # [[[1 4][2 5][3 6]]]

# np.ones / np.zeros — create filled arrays
C = np.ones((2, 2, 3))
D = np.zeros((2, 2, 3))
result = np.concatenate((C, D), axis=2)
print(result.shape)    # (2, 2, 6)  — grew along depth axis

# ✅ TASK: Stack two 1D arrays vertically. Then concatenate them horizontally.


# %%
# ── 1.9 Splitting Arrays ──────────────────────────
# array_split → split into N sub-arrays (handles uneven splits)
# split()     → same but CRASHES on uneven — use array_split instead

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)               # [array([1,2]), array([3,4]), array([5,6])]
print(newarr[0], newarr[1], newarr[2])

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],
                [10,11,12],[13,14,15],[16,17,18]])
print(np.array_split(arr, 3))              # split rows into 3 groups
print(np.array_split(arr, 3, axis=1))     # split columns into 3 groups

# ✅ TASK: Split np.arange(1, 11) into 4 parts. What does the last part contain?


# %%
# ── 1.10 Searching & Sorting ──────────────────────
# np.where      → returns INDICES where condition is True
# np.searchsorted → binary search on a sorted array (insertion point)
# np.sort       → returns a sorted COPY  (original unchanged)

arr = np.array([1, 2, 3, 4, 5, 4, 4])
print(np.where(arr == 4))            # (array([3, 5, 6]),)

arr = np.array([10, 14, 93, 41, 8, 7])
print(np.where(arr % 2 == 1))        # indices of odd numbers

arr = np.array([6, 7, 8, 9])
print(np.searchsorted(arr, 7))       # 1  — insert before index 1

arr = np.array([1, 3, 5, 7])
print(np.searchsorted(arr, [2, 4, 6], side='right'))  # [1 2 3]

print(np.sort(np.array([3, 2, 0, 1])))            # [0 1 2 3]
print(np.sort(np.array([[3, 2, 4], [5, 0, 1]])))  # sorts each row

# ✅ TASK: Find indices where values are even in [10,14,93,41,8,7].


# %%
# ── 1.11 Boolean Filtering ────────────────────────
# Pass a bool array/mask as index → only True positions returned.
# Direct expression like arr[arr > 42] is the clean, fast way.

arr = np.array([41, 42, 43, 44])

# Method 1: manual mask
print(arr[[True, False, True, False]])   # [41 43]

# Method 2: loop (verbose — just for learning)
filter_arr = []
for x in arr:
    filter_arr.append(True if x > 42 else False)
print(arr[filter_arr])   # [43 44]

# Method 3: direct expression — preferred ✅
print(arr[arr > 42])     # [43 44]

filter_arr = arr > 42    # the mask itself is an array of booleans
print(filter_arr)        # [False False  True  True]
print(arr[filter_arr])   # [43 44]

# ✅ TASK 1: Filter even numbers from [41, 42, 43, 44, 45, 46].
# ✅ TASK 2: Given arr = np.arange(1, 21), keep only multiples of 3.


# %%
# ── 1.12 Universal Functions (ufuncs) ────────────
# ufuncs apply an operation to EVERY element simultaneously.
# Built in C → much faster than Python loops.
# np.add, subtract, mod, divmod, absolute are all ufuncs.

x = [1, 2, 3, 4];  y = [4, 5, 6, 7]
print(np.add(x, y))        # [5 7 9 11]

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([ 3,  7,  9,  8,  2, 33])
print(np.mod(arr1, arr2))          # remainder
print(np.divmod(arr1, arr2))       # (quotient, remainder) as 2 arrays

arr = np.array([-1, -2, 1, 2, 3, -4])
print(np.absolute(arr))            # [1 2 1 2 3 4]

# frompyfunc — wrap a Python function to behave like a ufunc
def myadd(x, y):
    return x + y
myadd_uf = np.frompyfunc(myadd, 2, 1)  # 2 inputs, 1 output
print(myadd_uf([1,2,3,4], [5,6,7,8]))  # [6 8 10 12]

print(type(np.add))          # <class 'numpy.ufunc'>
print(type(np.concatenate))  # <class 'builtin_function_or_method'>

# ✅ TASK: Use np.multiply and np.divide on two arrays. Use frompyfunc to
#          wrap a multiply function and verify it gives the same result.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  PART 2 — IMAGE PROCESSING & COMPUTER VISION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Every image is just a NumPy array.
# Grayscale  →  shape (H, W)        pixel values 0–255
# RGB colour →  shape (H, W, 3)     3 channels: R, G, B
# Batch      →  shape (N, H, W, 3)  N images packed together
# dtype uint8  →  pixel range 0–255   (raw image from file/camera)
# dtype float32 → pixel range 0.0–1.0 (after normalisation for ML)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# %%
# ── 2.1 Images as Arrays ──────────────────────────
# np.zeros → black image  |  np.ones * 255 → white image
# shape = (H, W, C)   dtype = uint8   is the standard format.

H, W = 6, 8
black = np.zeros((H, W, 3), dtype=np.uint8)
print("Black image shape :", black.shape)    # (6, 8, 3)
print("dtype             :", black.dtype)    # uint8
print("Min / Max         :", black.min(), black.max())   # 0  0

white = np.ones((H, W, 3), dtype=np.uint8) * 255
print("White min/max     :", white.min(), white.max())   # 255  255

# Pure red image: only channel 0 (R) = 255, others = 0
red = np.zeros((H, W, 3), dtype=np.uint8)
red[:, :, 0] = 255
print("Red pixel [0,0]   :", red[0, 0])    # [255   0   0]

# ✅ TASK: Create a pure blue (0, 0, 255) image of size 4×6. Check one pixel.


# %%
# ── 2.2 Pixel Access, Modification & Cropping ────
# Indexing accesses pixels.  Slicing crops regions.
# ⚠️  Slicing returns a VIEW — use .copy() to stay safe.

np.random.seed(0)
img = np.zeros((8, 8, 3), dtype=np.uint8)

# Write individual pixels
img[0, 0] = [255, 0,   0]      # top-left = red
img[0, 1] = [0,   255, 0]      # next     = green
img[0, 2] = [0,   0,   255]    # next     = blue
print("Top row (first 3 pixels):\n", img[0, :3])

# Write a whole row / column
img[4, :]    = [255, 255, 0]   # row 4 = yellow
img[:, 4]    = [128, 0,  128]  # col 4 = purple
img[2:5, 2:6] = [0, 200, 200]  # rectangle = teal

# Cropping = slicing  (produces a VIEW)
crop = img[2:6, 2:6]           # 4×4 region
print("Crop shape:", crop.shape)    # (4, 4, 3)

# ⚠️  Modifying the crop modifies img too (it's a view!)
safe_crop = img[2:6, 2:6].copy()   # independent copy
safe_crop[0, 0] = [0, 0, 0]        # black dot on copy only
print("img[2,2] unchanged:", img[2, 2])   # [0 200 200] — not affected

# ✅ TASK 1: Draw a white cross on an 8×8 black image
#            (set the middle row and middle column to 255).
# ✅ TASK 2: Crop the bottom-right 4×4 from a 8×8 image using slicing.


# %%
# ── 2.3 Channel Splitting & Merging ──────────────
# Indexing on axis=2 extracts individual colour channels.
# np.stack reassembles channels back into a (H,W,3) image.

np.random.seed(1)
img = (np.ones((4, 5, 3), dtype=np.uint8) * [100, 150, 200])
print("One pixel:", img[0, 0])   # [100 150 200]

R = img[:, :, 0]    # Red   channel → shape (4, 5)
G = img[:, :, 1]    # Green channel
B = img[:, :, 2]    # Blue  channel
print("R shape:", R.shape, "| R mean:", R.mean())   # 4×5  |  100.0

# Merge back: np.stack creates (H, W, 3) from three (H, W) arrays
merged = np.stack([R, G, B], axis=2)
print("Same as original:", np.array_equal(img, merged))   # True

# Swap R and B → converts RGB to BGR (OpenCV format)
bgr = np.stack([B, G, R], axis=2)
print("BGR pixel [0,0]:", bgr[0, 0])   # [200 150 100]

# Zero out a channel: keep only red
red_only = img.copy()
red_only[:, :, 1] = 0   # zero green
red_only[:, :, 2] = 0   # zero blue
print("Red-only pixel:", red_only[0, 0])   # [100   0   0]

# ✅ TASK: Split an image, multiply the G channel by 2 (clip at 255 manually
#          using boolean filter), then merge back.


# %%
# ── 2.4 Grayscale Conversion ──────────────────────
# Human eyes are most sensitive to green, then red, then blue.
# ITU-R BT.601 formula:  Gray = 0.299×R + 0.587×G + 0.114×B
# ⚠️  Cast to float32 FIRST — uint8 overflows silently above 255!

np.random.seed(2)
img = np.random.randint(50, 200, (4, 5, 3), dtype=np.uint8)

# ⚠️  Overflow demo — why float32 matters
bad  = np.uint8(200) + np.uint8(100)   # wraps at 256!
good = np.float32(200) + np.float32(100)
print("uint8 overflow:", bad)    # 44  — WRONG
print("float32 safe  :", good)   # 300.0  — correct

# Correct grayscale conversion
R = img[:, :, 0].astype(np.float32)
G = img[:, :, 1].astype(np.float32)
B = img[:, :, 2].astype(np.float32)
gray = (0.299 * R + 0.587 * G + 0.114 * B).astype(np.uint8)
print("Gray shape:", gray.shape)   # (4, 5) — no channel axis
print("Gray:\n", gray)

# np.absolute — useful for difference images (edge-like detection)
img1 = np.array([[100, 200], [50, 80]], dtype=np.int32)
img2 = np.array([[80,  210], [90, 60]], dtype=np.int32)
diff = np.absolute(img1 - img2).astype(np.uint8)
print("Pixel difference:\n", diff)   # [20 10][40 20]

# ✅ TASK 1: Apply the ITU-R formula to a 5×5 random RGB image.
# ✅ TASK 2: Compute np.absolute(img_a - img_b) for two random images.
#            Large values = big differences = "edges" or "motion".


# %%
# ── 2.5 Normalisation & Thresholding ─────────────
# Normalisation: uint8 [0–255] → float32 [0.0–1.0]   (for ML models)
# Thresholding:  set pixels above T to 255, rest to 0 (segmentation)
# Both use astype() and np.where — already seen in Part 1.

img = np.array([[0, 128, 255],
                [64, 192,  32]], dtype=np.uint8)

# uint8 → float32
img_f = img.astype(np.float32) / 255.0
print("float32:\n", img_f)
print("min:", img_f.min(), "max:", img_f.max())   # 0.0  1.0

# float32 → uint8 (back to original)
img_back = (img_f * 255.0).astype(np.uint8)
print("Restored:", np.array_equal(img, img_back))   # True

# Binary thresholding using np.where
gray = np.array([[100, 200,  50, 180],
                 [ 30,  90, 210, 140],
                 [170,  60, 130,  20]], dtype=np.uint8)
binary = np.where(gray > 128, 255, 0).astype(np.uint8)
print("Binary threshold:\n", binary)
# pixels > 128 → 255 (white), rest → 0 (black)

# Boolean mask — keep bright pixels, zero dark ones
np.random.seed(3)
img_c = np.random.randint(0, 256, (6, 6, 3), dtype=np.uint8)
gray2 = (img_c[:,:,0].astype(np.float32) * 0.299 +
         img_c[:,:,1].astype(np.float32) * 0.587 +
         img_c[:,:,2].astype(np.float32) * 0.114).astype(np.uint8)
mask = gray2 > 128
result = img_c.copy()
result[~mask] = 0      # zero out dark pixels
print("Bright-pixel-only result, pixel (0,0):", result[0, 0])

# ✅ TASK 1: Threshold a grayscale image at 100. Verify the binary output.
# ✅ TASK 2: Normalise a uint8 image to float32, then back to uint8.
#            Check if the round-trip is lossless.


# %%
# ── 2.6 Flipping — Data Augmentation ─────────────
# Flipping creates extra training data at zero cost.
# A flipped image of a cat is still a cat!
# All flips are slicing tricks → they return VIEWS (fast, no copy).

img = np.arange(1, 25, dtype=np.uint8).reshape(4, 6)
print("Original:\n", img)

hflip = img[:, ::-1]          # left ↔ right
vflip = img[::-1, :]          # top  ↔ bottom
both  = img[::-1, ::-1]       # 180° rotation

print("H-flip:\n", hflip)
print("V-flip:\n", vflip)
print("Both:\n", both)

# For colour images — channels axis is untouched
img_c = np.zeros((4, 6, 3), dtype=np.uint8)
img_c[:, :, 0] = np.arange(24).reshape(4, 6)   # R gradient

hflip_c = img_c[:, ::-1, :]   # flip W axis only, keep C
vflip_c = img_c[::-1, :, :]   # flip H axis only, keep C
print("Colour H-flip shape:", hflip_c.shape)   # (4, 6, 3)

# ✅ TASK 1: Flip a 4×6 image horizontally then vertically.
#            Verify double-flip returns the original.
# ✅ TASK 2: Flip only the R channel of a colour image horizontally.


# %%
# ── 2.7 Combining Images & Batch Stacking ─────────
# hstack / vstack → place images side by side or top-to-bottom
# np.stack        → build a batch (N, H, W, C)  for deep learning
# concatenate     → same as hstack/vstack but explicit axis control

np.random.seed(4)
img_a = np.random.randint(0, 256, (4, 4, 3), dtype=np.uint8)
img_b = np.random.randint(0, 256, (4, 4, 3), dtype=np.uint8)

side_by_side = np.concatenate([img_a, img_b], axis=1)  # (4, 8, 3)
stacked_vert = np.vstack([img_a, img_b])                # (8, 4, 3)
print("Side-by-side shape:", side_by_side.shape)
print("Vertical stack    :", stacked_vert.shape)

# Split a panorama back into two halves
left, right = np.array_split(side_by_side, 2, axis=1)
print("Split back — left:", left.shape, "right:", right.shape)

# Build a BATCH: shape (N, H, W, C)
img_c = np.random.randint(0, 256, (4, 4, 3), dtype=np.uint8)
img_d = np.random.randint(0, 256, (4, 4, 3), dtype=np.uint8)
batch = np.stack([img_a, img_b, img_c, img_d], axis=0)  # N=4
print("Batch shape:", batch.shape)   # (4, 4, 4, 3)

# Normalise the whole batch at once with astype
batch_f = batch.astype(np.float32) / 255.0
print("Batch float32 — min:", batch_f.min(), "max:", batch_f.max())

# Access one image from the batch
print("Image 2 shape:", batch[2].shape)   # (4, 4, 3)

# ✅ TASK 1: Build a batch of 8 images (each 6×6×3 uint8) using np.stack.
#            Normalise the whole batch to float32 in ONE operation.
# ✅ TASK 2: From a batch of 6 images, split into two mini-batches of 3.


# ============================================================
#  SUMMARY
#  PART 1 — NumPy Basics
#   1.1 Array Creation & Attributes  (ndim, shape, ndmin)
#   1.2 Indexing                     (1D / 2D / 3D / negative)
#   1.3 Slicing                      (start:stop:step, 2D)
#   1.4 Data Types & astype()        (i4, f, bool, U6)
#   1.5 Copy vs View                 (.copy, .view, .base)
#   1.6 Reshape                      (reshape, -1, 3D)
#   1.7 Iteration                    (for, nditer, ndenumerate)
#   1.8 Joining                      (concatenate, stack, h/v/dstack)
#   1.9 Splitting                    (array_split, axis=1)
#   1.10 Searching & Sorting         (where, searchsorted, sort)
#   1.11 Boolean Filtering           (mask, direct expression)
#   1.12 ufuncs                      (add, subtract, mod, absolute, frompyfunc)
#
#  PART 2 — Image Processing (NumPy only)
#   2.1 Images as arrays   → zeros/ones, shape (H,W,3), dtype uint8
#   2.2 Pixel access & crop → indexing, slicing, .copy() safety
#   2.3 Channel splitting  → arr[:,:,i], np.stack to merge back
#   2.4 Grayscale          → float32 weighted add, np.absolute for diff
#   2.5 Normalise & threshold → /255.0, astype, np.where, bool mask
#   2.6 Flipping           → [::-1] slicing, data augmentation
#   2.7 Combine & batch    → hstack/vstack/concatenate, np.stack (N,H,W,C)
# ============================================================
print("✅ NumPy file complete.")

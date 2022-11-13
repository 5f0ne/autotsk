# Description

Automatically creates mmls, fsstat and fls results for image files

# Installation
```bash
# Sleuthkit needs to be installed 
# and available in PATH
sudo apt install sleuthkit 
pip install autotsk
```

# Usage

**From command line:**

`python -m autotsk --path PATH [--result RESULT]`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path to img/dd file |
|--result | -r | String | ./autotsk-result | Path to result dir |


# Example

`python -m autotsk -p example.dd`

```
################################################################################

autotsk by 5f0
Automatically creates mmls, fsstat and fls results for image files

Current working directory: /path/to/autotsk

 Datetime: 01/01/1970 10:11:12

################################################################################

mmls Output
----------

DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000008191   0000008192   Unallocated
002:  000:000   0000008192   0000110591   0000102400   Win95 FAT32 (0x0b)
003:  -------   0000110592   0000212991   0000102400   Unallocated
004:  000:001   0000212992   0000458751   0000245760   NTFS / exFAT (0x07)
005:  -------   0000458752   0000466943   0000008192   Unallocated
006:  000:002   0000466944   0000569343   0000102400   Linux (0x83)
007:  -------   0000569344   0000577535   0000008192   Unallocated
008:  000:003   0000577536   0000782335   0000204800   Linux (0x83)
009:  -------   0000782336   0003911679   0003129344   Unallocated



Extracting Offsets
----------

Offset found: 8192
Offset found: 212992
Offset found: 466944
Offset found: 577536



Applying TSK Commands
----------

fsstat and fls for offset: 8192
fsstat and fls for offset: 212992
fsstat and fls for offset: 466944
fsstat and fls for offset: 577536



Result Location
----------

Path: ./autotsk-result

################################################################################

Execution Time: 0.075163 sec
```

Created files in result directory:

```
autotsk-result/
├── 0-8192-fls.txt
├── 0-8192-fsstat.txt
├── 1-212992-fls.txt
├── 1-212992-fsstat.txt
├── 2-466944-fls.txt
├── 2-466944-fsstat.txt
├── 3-577536-fls.txt
├── 3-577536-fsstat.txt
└── mmls.txt
```

# License

MIT
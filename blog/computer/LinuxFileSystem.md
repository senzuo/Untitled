# 使用哪一个Linux文件系统

![](https://www.howtogeek.com/wp-content/uploads/2017/02/ximg_58af3af6f2b60.png.pagespeed.gp+jp+jw+pj+ws+js+rj+rp+rw+ri+cp+md.ic.3cfVRpwG9U.png)

文件系统是使用Linux的人一定要掌握的。Windows用户完全不用担心，默认NTFS，但在Linux PC上，格式化分区时会看到一系列文件系统，不同的文件系统会如何影响计算机，应该怎样选择文件系统类型呢？

## 傻瓜式答案：如果不确定用Ext4

如果不确定，那么就使用Ext4吧！

选择Ext4的一个原因是在绝大多数的Linux版本默认Ext4，Ext4是Ext3文件系统的提升，Ext4不是最新的文件系统，但是Ext4稳定、可靠。

未来Linux版本将会逐渐移向BtrFS，BtrFS还非常前沿在发展中。

注意：如果你格式化一个想在别的操作系统上分享文件的外部驱动，那么就不可以使用Ext4，因为Windows和macOS无法读取Ext4文件系统，应该使用exFAT或者FAT32

分区的时候也应该创造一个几个GB的swap分区，顾名思义用于交换，类似于Windows的paging file，当RAM使用完的时候就在swap区交换，且该分区必须格式化为 `swap`

![](https://www.howtogeek.com/wp-content/uploads/2017/02/ximg_58af3c7ed031b.png.pagespeed.gp+jp+jw+pj+ws+js+rj+rp+rw+ri+cp+md.ic.xzuo4SFc7v.png)

## 什么是Journaling

当选择文件系统的时候，你需要注意的是有点被标记为“Journaling”，有的没有，这一点非常重要。

Journaling被用于防止因为碰撞和突然掉电造成的数据缺失。假设系统正往硬盘写入文件，突然掉电了！没有Journaling，计算机就不知道文件是否完全被写入硬盘。文件将会烂死与硬盘。

但是有Journal的话，计算机就记下来会写一个确切的文件到硬盘，文件写入完成，然后就从Journal中删除该记录。如果中途掉电，当重新上电的时候，Linux将会检查文件系统的Journal，重新开始没有完成的任务。

每一个现代文件系统都支持Journal，不支持Journal的文件系统被用于高性能服务器或者系统管理员想节约出额外的性能

## 所有的Linux文件系统都有什么不同

任何有能力有时间的人都可以开发一个新的Linux文件系统，所有Linux文件系统会有如此多的选项。

### Ext

`Extended file system`，是第一个被Linux使用的文件系统，有四个版本，Ext是Minix文件系统的提升，选择许多Linux版本都不在支持了。

### Ext2

Ext2是一个不支持journaling的文件系统，第一个支持2T文件大小，缺少Journal意味着写操作更少，这也使得该文件系统对于闪存（USB）更有用，除非知道因为某些原因使用Ext2，否则不推荐使用。

### Ext3

Ext3向后兼容Ext2，基本上就是Ext2 + Journal

### Ext4

Ext4也向后兼容，你可以挂载一个Ext4文件系统作为Ext3或者挂载Ext3、Ext2作为Ext4。包括更新的特点：减少文件碎片，允许更大的文件，使用延时分配提高闪存生命。这是最新版本的EXT文件系统，是大多数Linux发行版的默认版本。

### BtrFS

最初由甲骨文设计的文件系统，B-Tree File System，支持drive pooling, on the fly snapshots, transparent compression, and online defragmentation
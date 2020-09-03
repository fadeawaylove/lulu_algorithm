# Redis问题汇总

<!-- TOC -->

- [Redis问题汇总](#redis问题汇总)
    - [1.Redis是什么？](#1redis是什么)
    - [2.Redis有哪些数据结构？](#2redis有哪些数据结构)

<!-- /TOC -->

## 1.Redis是什么？
1. 是一个完全开源免费的`key-value`内存数据库
2. 通常被认为是一个数据结构服务起，主要是因为其有着丰富的数据结构string（字符串）、hash（哈希）、list（列表）、set（集合）、zset（有序集合）

## 2.Redis有哪些数据结构？
1. 常用数据结构
    - 字符串
    - 列表
    - 字典
    - 集合
    - 有序集合
2. 高级数据结构
    - HyperLogLog：不精确的去重计数（一个热点页面的去重访问次数，即页面海量访问的UV），原理根据最长单一事件的概率，反算基数（使用分桶优化为LogLog算法，使用调和平均数优化为HyperLogLog算法）
    - GeoHash：经纬度计算距离
    - Pub/Sub：发布订阅模式，缺点是消费者下线则会漏消费
3. Redis Module（Redis模块）
    - BloomFilter：布隆过滤器，原理是多hash取模算下标，用于去重判断
    - RedisSearch：一个搜索引擎，不使用内部数据结构
    - Redis-ML：机器学习服务引擎
    - Redis-Cell：Redis提供的限流模块，原理是漏斗算法


    
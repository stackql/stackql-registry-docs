---
title: configs
hide_title: false
hide_table_of_contents: false
keywords:
  - configs
  - databases
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="_backup_hour" /> | `integer` | The hour of day (in UTC) when backup for the service starts. New backup only starts if previous backup has already completed. |
| <CopyableCode code="_backup_minute" /> | `integer` | The minute of the backup hour when backup for the service starts. New backup is only started if previous backup has already completed. |
| <CopyableCode code="action_auto_create_index_enabled" /> | `boolean` | Specifices whether to allow automatic creation of indices. |
| <CopyableCode code="action_destructive_requires_name" /> | `boolean` | Specifies whether to require explicit index names when deleting indices. |
| <CopyableCode code="auto_create_topics_enable" /> | `boolean` | Enable auto creation of topics |
| <CopyableCode code="autovacuum_analyze_scale_factor" /> | `number` | Specifies a fraction, in a decimal value, of the table size to add to autovacuum_analyze_threshold when deciding whether to trigger an ANALYZE. The default is 0.2 (20% of table size). |
| <CopyableCode code="autovacuum_analyze_threshold" /> | `integer` | Specifies the minimum number of inserted, updated, or deleted tuples needed to trigger an ANALYZE in any one table. The default is 50 tuples. |
| <CopyableCode code="autovacuum_freeze_max_age" /> | `integer` | Specifies the maximum age (in transactions) that a table's pg_class.relfrozenxid field can attain before a VACUUM operation is forced to prevent transaction ID wraparound within the table. Note that the system will launch autovacuum processes to prevent wraparound even when autovacuum is otherwise disabled. This parameter will cause the server to be restarted. |
| <CopyableCode code="autovacuum_max_workers" /> | `integer` | Specifies the maximum number of autovacuum processes (other than the autovacuum launcher) that may be running at any one time. The default is three. This parameter can only be set at server start. |
| <CopyableCode code="autovacuum_naptime" /> | `integer` | Specifies the minimum delay, in seconds, between autovacuum runs on any given database. The default is one minute. |
| <CopyableCode code="autovacuum_vacuum_cost_delay" /> | `integer` | Specifies the cost delay value, in milliseconds, that will be used in automatic VACUUM operations. If -1, uses the regular vacuum_cost_delay value, which is 20 milliseconds. |
| <CopyableCode code="autovacuum_vacuum_cost_limit" /> | `integer` | Specifies the cost limit value that will be used in automatic VACUUM operations. If -1 is specified (which is the default), the regular vacuum_cost_limit value will be used. |
| <CopyableCode code="autovacuum_vacuum_scale_factor" /> | `number` | Specifies a fraction, in a decimal value, of the table size to add to autovacuum_vacuum_threshold when deciding whether to trigger a VACUUM. The default is 0.2 (20% of table size). |
| <CopyableCode code="autovacuum_vacuum_threshold" /> | `integer` | Specifies the minimum number of updated or deleted tuples needed to trigger a VACUUM in any one table. The default is 50 tuples. |
| <CopyableCode code="backup_hour" /> | `integer` | The hour of day (in UTC) when backup for the service starts. New backup only starts if previous backup has already completed. |
| <CopyableCode code="backup_minute" /> | `integer` | The minute of the backup hour when backup for the service starts. New backup only starts if previous backup has already completed. |
| <CopyableCode code="bgwriter_delay" /> | `integer` | Specifies the delay, in milliseconds, between activity rounds for the background writer. Default is 200 ms. |
| <CopyableCode code="bgwriter_flush_after" /> | `integer` | The amount of kilobytes that need to be written by the background writer before attempting to force the OS to issue these writes to underlying storage. Specified in kilobytes, default is 512. Setting of 0 disables forced writeback. |
| <CopyableCode code="bgwriter_lru_maxpages" /> | `integer` | The maximum number of buffers that the background writer can write. Setting this to zero disables background writing. Default is 100. |
| <CopyableCode code="bgwriter_lru_multiplier" /> | `number` | The average recent need for new buffers is multiplied by bgwriter_lru_multiplier to arrive at an estimate of the number that will be needed during the next round, (up to bgwriter_lru_maxpages). 1.0 represents a “just in time” policy of writing exactly the number of buffers predicted to be needed. Larger values provide some cushion against spikes in demand, while smaller values intentionally leave writes to be done by server processes. The default is 2.0. |
| <CopyableCode code="binlog_retention_period" /> | `number` | The minimum amount of time, in seconds, to keep binlog entries before deletion. This may be extended for services that require binlog entries for longer than the default, for example if using the MySQL Debezium Kafka connector. |
| <CopyableCode code="cluster_max_shards_per_node" /> | `integer` | Maximum number of shards allowed per data node. |
| <CopyableCode code="cluster_routing_allocation_node_concurrent_recoveries" /> | `integer` | Maximum concurrent incoming/outgoing shard recoveries (normally replicas) are allowed to happen per node . |
| <CopyableCode code="compression_type" /> | `string` | Specify the final compression type for a given topic. This configuration accepts the standard compression codecs ('gzip', 'snappy', 'lz4', 'zstd'). It additionally accepts 'uncompressed' which is equivalent to no compression; and 'producer' which means retain the original compression codec set by the producer. |
| <CopyableCode code="connect_timeout" /> | `integer` | The number of seconds that the mysqld server waits for a connect packet before responding with bad handshake. |
| <CopyableCode code="connections_max_idle_ms" /> | `integer` | Idle connections timeout: the server socket processor threads close the connections that idle for longer than this. |
| <CopyableCode code="deadlock_timeout" /> | `integer` | The amount of time, in milliseconds, to wait on a lock before checking to see if there is a deadlock condition. |
| <CopyableCode code="default_read_concern" /> | `string` | Specifies the default consistency behavior of reads from the database. Data that is returned from the query with may or may not have been acknowledged by all nodes in the replicaset depending on this value. Learn more [here](https://www.mongodb.com/docs/manual/reference/read-concern/). |
| <CopyableCode code="default_replication_factor" /> | `integer` | Replication factor for autocreated topics |
| <CopyableCode code="default_time_zone" /> | `string` | Default server time zone, in the form of an offset from UTC (from -12:00 to +12:00), a time zone name (EST), or 'SYSTEM' to use the MySQL server default. |
| <CopyableCode code="default_toast_compression" /> | `string` | Specifies the default TOAST compression method for values of compressible columns (the default is lz4). |
| <CopyableCode code="default_write_concern" /> | `string` | Describes the level of acknowledgment requested from MongoDB for write operations clusters. This field can set to either `majority` or a number `0...n` which will describe the number of nodes that must acknowledge the write operation before it is fully accepted. Setting to `0` will request no acknowledgement of the write operation. Learn more [here](https://www.mongodb.com/docs/manual/reference/write-concern/). |
| <CopyableCode code="enable_security_audit" /> | `boolean` | Specifies whether to allow security audit logging. |
| <CopyableCode code="group_concat_max_len" /> | `integer` | The maximum permitted result length, in bytes, for the GROUP_CONCAT() function. |
| <CopyableCode code="group_initial_rebalance_delay_ms" /> | `integer` | The amount of time, in milliseconds, the group coordinator will wait for more consumers to join a new group before performing the first rebalance. A longer delay means potentially fewer rebalances, but increases the time until processing begins. The default value for this is 3 seconds. During development and testing it might be desirable to set this to 0 in order to not delay test execution time. |
| <CopyableCode code="group_max_session_timeout_ms" /> | `integer` | The maximum allowed session timeout for registered consumers. Longer timeouts give consumers more time to process messages in between heartbeats at the cost of a longer time to detect failures. |
| <CopyableCode code="group_min_session_timeout_ms" /> | `integer` | The minimum allowed session timeout for registered consumers. Longer timeouts give consumers more time to process messages in between heartbeats at the cost of a longer time to detect failures. |
| <CopyableCode code="http_max_content_length_bytes" /> | `integer` | Maximum content length for HTTP requests to the OpenSearch HTTP API, in bytes. |
| <CopyableCode code="http_max_header_size_bytes" /> | `integer` | Maximum size of allowed headers, in bytes. |
| <CopyableCode code="http_max_initial_line_length_bytes" /> | `integer` | Maximum length of an HTTP URL, in bytes. |
| <CopyableCode code="idle_in_transaction_session_timeout" /> | `integer` | Time out sessions with open transactions after this number of milliseconds |
| <CopyableCode code="indices_fielddata_cache_size_percentage" /> | `integer` | Maximum amount of heap memory used for field data cache, expressed as a percentage. Decreasing the value too much will increase overhead of loading field data. Increasing the value too much will decrease amount of heap available for other operations. |
| <CopyableCode code="indices_memory_index_buffer_size_percentage" /> | `integer` | Total amount of heap used for indexing buffer before writing segments to disk, expressed as a percentage. Too low value will slow down indexing; too high value will increase indexing performance but causes performance issues for query performance. |
| <CopyableCode code="indices_memory_max_index_buffer_size_mb" /> | `integer` | Maximum amount of heap used for indexing buffer before writing segments to disk, in mb. Works in conjunction with indices_memory_index_buffer_size_percentage, each being enforced. The default is unbounded. |
| <CopyableCode code="indices_memory_min_index_buffer_size_mb" /> | `integer` | Minimum amount of heap used for indexing buffer before writing segments to disk, in mb. Works in conjunction with indices_memory_index_buffer_size_percentage, each being enforced. |
| <CopyableCode code="indices_queries_cache_size_percentage" /> | `integer` | Maximum amount of heap used for query cache. Too low value will decrease query performance and increase performance for other operations; too high value will cause issues with other functionality. |
| <CopyableCode code="indices_query_bool_max_clause_count" /> | `integer` | Maximum number of clauses Lucene BooleanQuery can have. Only increase it if necessary, as it may cause performance issues. |
| <CopyableCode code="indices_recovery_max_concurrent_file_chunks" /> | `integer` | Maximum number of file chunks sent in parallel for each recovery. |
| <CopyableCode code="indices_recovery_max_mb_per_sec" /> | `integer` | Limits total inbound and outbound recovery traffic for each node, expressed in mb per second. Applies to both peer recoveries as well as snapshot recoveries (i.e., restores from a snapshot). |
| <CopyableCode code="information_schema_stats_expiry" /> | `integer` | The time, in seconds, before cached statistics expire. |
| <CopyableCode code="innodb_change_buffer_max_size" /> | `integer` | Specifies the maximum size of the InnoDB change buffer as a percentage of the buffer pool. |
| <CopyableCode code="innodb_flush_neighbors" /> | `integer` | Specifies whether flushing a page from the InnoDB buffer pool also flushes other dirty pages in the same extent. - 0 &mdash; disables this functionality, dirty pages in the same extent are not flushed. - 1 &mdash; flushes contiguous dirty pages in the same extent. - 2 &mdash; flushes dirty pages in the same extent. |
| <CopyableCode code="innodb_ft_min_token_size" /> | `integer` | The minimum length of words that an InnoDB FULLTEXT index stores. |
| <CopyableCode code="innodb_ft_server_stopword_table" /> | `string` | The InnoDB FULLTEXT index stopword list for all InnoDB tables. |
| <CopyableCode code="innodb_lock_wait_timeout" /> | `integer` | The time, in seconds, that an InnoDB transaction waits for a row lock. before giving up. |
| <CopyableCode code="innodb_log_buffer_size" /> | `integer` | The size of the buffer, in bytes, that InnoDB uses to write to the log files. on disk. |
| <CopyableCode code="innodb_online_alter_log_max_size" /> | `integer` | The upper limit, in bytes, of the size of the temporary log files used during online DDL operations for InnoDB tables. |
| <CopyableCode code="innodb_print_all_deadlocks" /> | `boolean` | When enabled, records information about all deadlocks in InnoDB user transactions in the error log. Disabled by default. |
| <CopyableCode code="innodb_read_io_threads" /> | `integer` | The number of I/O threads for read operations in InnoDB. Changing this parameter will lead to a restart of the MySQL service. |
| <CopyableCode code="innodb_rollback_on_timeout" /> | `boolean` | When enabled, transaction timeouts cause InnoDB to abort and roll back the entire transaction. |
| <CopyableCode code="innodb_thread_concurrency" /> | `integer` | Defines the maximum number of threads permitted inside of InnoDB. A value of 0 (the default) is interpreted as infinite concurrency (no limit). This variable is intended for performance tuning on high concurrency systems. |
| <CopyableCode code="innodb_write_io_threads" /> | `integer` | The number of I/O threads for write operations in InnoDB. Changing this parameter will lead to a restart of the MySQL service. |
| <CopyableCode code="interactive_timeout" /> | `integer` | The time, in seconds, the server waits for activity on an interactive. connection before closing it. |
| <CopyableCode code="internal_tmp_mem_storage_engine" /> | `string` | The storage engine for in-memory internal temporary tables. |
| <CopyableCode code="ism_enabled" /> | `boolean` | Specifies whether ISM is enabled or not. |
| <CopyableCode code="ism_history_enabled" /> | `boolean` | Specifies whether audit history is enabled or not. The logs from ISM are automatically indexed to a logs document. |
| <CopyableCode code="ism_history_max_age_hours" /> | `integer` | Maximum age before rolling over the audit history index, in hours. |
| <CopyableCode code="ism_history_max_docs" /> | `integer` | Maximum number of documents before rolling over the audit history index. |
| <CopyableCode code="ism_history_rollover_check_period_hours" /> | `integer` | The time between rollover checks for the audit history index, in hours. |
| <CopyableCode code="ism_history_rollover_retention_period_days" /> | `integer` | Length of time long audit history indices are kept, in days. |
| <CopyableCode code="jit" /> | `boolean` | Activates, in a boolean, the system-wide use of Just-in-Time Compilation (JIT). |
| <CopyableCode code="log_autovacuum_min_duration" /> | `integer` | Causes each action executed by autovacuum to be logged if it ran for at least the specified number of milliseconds. Setting this to zero logs all autovacuum actions. Minus-one (the default) disables logging autovacuum actions. |
| <CopyableCode code="log_cleaner_delete_retention_ms" /> | `integer` | How long are delete records retained? |
| <CopyableCode code="log_cleaner_max_compaction_lag_ms" /> | `integer` | The maximum amount of time message will remain uncompacted. Only applicable for logs that are being compacted |
| <CopyableCode code="log_cleaner_min_cleanable_ratio" /> | `number` | Controls log compactor frequency. Larger value means more frequent compactions but also more space wasted for logs. Consider setting log_cleaner_max_compaction_lag_ms to enforce compactions sooner, instead of setting a very high value for this option. |
| <CopyableCode code="log_cleaner_min_compaction_lag_ms" /> | `integer` | The minimum time a message will remain uncompacted in the log. Only applicable for logs that are being compacted. |
| <CopyableCode code="log_cleanup_policy" /> | `string` | The default cleanup policy for segments beyond the retention window |
| <CopyableCode code="log_error_verbosity" /> | `string` | Controls the amount of detail written in the server log for each message that is logged. |
| <CopyableCode code="log_flush_interval_messages" /> | `integer` | The number of messages accumulated on a log partition before messages are flushed to disk |
| <CopyableCode code="log_flush_interval_ms" /> | `integer` | The maximum time in ms that a message in any topic is kept in memory before flushed to disk. If not set, the value in log.flush.scheduler.interval.ms is used |
| <CopyableCode code="log_index_interval_bytes" /> | `integer` | The interval with which Kafka adds an entry to the offset index |
| <CopyableCode code="log_index_size_max_bytes" /> | `integer` | The maximum size in bytes of the offset index |
| <CopyableCode code="log_line_prefix" /> | `string` | Selects one of the available log-formats. These can support popular log analyzers like pgbadger, pganalyze, etc. |
| <CopyableCode code="log_message_downconversion_enable" /> | `boolean` | This configuration controls whether down-conversion of message formats is enabled to satisfy consume requests. |
| <CopyableCode code="log_message_timestamp_difference_max_ms" /> | `integer` | The maximum difference allowed between the timestamp when a broker receives a message and the timestamp specified in the message |
| <CopyableCode code="log_message_timestamp_type" /> | `string` | Define whether the timestamp in the message is message create time or log append time. |
| <CopyableCode code="log_min_duration_statement" /> | `integer` | Log statements that take more than this number of milliseconds to run. If -1, disables. |
| <CopyableCode code="log_preallocate" /> | `boolean` | Controls whether to preallocate a file when creating a new segment |
| <CopyableCode code="log_retention_bytes" /> | `integer` | The maximum size of the log before deleting messages |
| <CopyableCode code="log_retention_hours" /> | `integer` | The number of hours to keep a log file before deleting it |
| <CopyableCode code="log_retention_ms" /> | `integer` | The number of milliseconds to keep a log file before deleting it (in milliseconds), If not set, the value in log.retention.minutes is used. If set to -1, no time limit is applied. |
| <CopyableCode code="log_roll_jitter_ms" /> | `integer` | The maximum jitter to subtract from logRollTimeMillis (in milliseconds). If not set, the value in log.roll.jitter.hours is used |
| <CopyableCode code="log_roll_ms" /> | `integer` | The maximum time before a new log segment is rolled out (in milliseconds). |
| <CopyableCode code="log_segment_bytes" /> | `integer` | The maximum size of a single log file |
| <CopyableCode code="log_segment_delete_delay_ms" /> | `integer` | The amount of time to wait before deleting a file from the filesystem |
| <CopyableCode code="long_query_time" /> | `number` | The time, in seconds, for a query to take to execute before being captured by slow_query_logs. Default is 10 seconds. |
| <CopyableCode code="max_allowed_packet" /> | `integer` | The size of the largest message, in bytes, that can be received by the server. Default is 67108864 (64M). |
| <CopyableCode code="max_connections_per_ip" /> | `integer` | The maximum number of connections allowed from each ip address (defaults to 2147483647). |
| <CopyableCode code="max_failover_replication_time_lag" /> | `integer` | Number of seconds of master unavailability before triggering database failover to standby. The default value is 60. |
| <CopyableCode code="max_files_per_process" /> | `integer` | PostgreSQL maximum number of files that can be open per process. |
| <CopyableCode code="max_heap_table_size" /> | `integer` | The maximum size, in bytes, of internal in-memory tables. Also set tmp_table_size. Default is 16777216 (16M) |
| <CopyableCode code="max_incremental_fetch_session_cache_slots" /> | `integer` | The maximum number of incremental fetch sessions that the broker will maintain. |
| <CopyableCode code="max_locks_per_transaction" /> | `integer` | PostgreSQL maximum locks per transaction. Once increased, this parameter cannot be lowered from its set value. |
| <CopyableCode code="max_logical_replication_workers" /> | `integer` | PostgreSQL maximum logical replication workers (taken from the pool of max_parallel_workers). |
| <CopyableCode code="max_parallel_workers" /> | `integer` | Sets the maximum number of workers that the system can support for parallel queries. |
| <CopyableCode code="max_parallel_workers_per_gather" /> | `integer` | Sets the maximum number of workers that can be started by a single Gather or Gather Merge node. |
| <CopyableCode code="max_pred_locks_per_transaction" /> | `integer` | PostgreSQL maximum predicate locks per transaction. |
| <CopyableCode code="max_prepared_transactions" /> | `integer` | PostgreSQL maximum prepared transactions. Once increased, this parameter cannot be lowered from its set value. |
| <CopyableCode code="max_replication_slots" /> | `integer` | PostgreSQL maximum replication slots. |
| <CopyableCode code="max_stack_depth" /> | `integer` | Maximum depth of the stack in bytes. |
| <CopyableCode code="max_standby_archive_delay" /> | `integer` | Max standby archive delay in milliseconds. |
| <CopyableCode code="max_standby_streaming_delay" /> | `integer` | Max standby streaming delay in milliseconds. |
| <CopyableCode code="max_wal_senders" /> | `integer` | PostgreSQL maximum WAL senders. Once increased, this parameter cannot be lowered from its set value. |
| <CopyableCode code="max_worker_processes" /> | `integer` | Sets the maximum number of background processes that the system can support. Once increased, this parameter cannot be lowered from its set value. |
| <CopyableCode code="message_max_bytes" /> | `integer` | The maximum size of message that the server can receive. |
| <CopyableCode code="min_insync_replicas" /> | `integer` | When a producer sets acks to 'all' (or '-1'), min_insync_replicas specifies the minimum number of replicas that must acknowledge a write for the write to be considered successful. |
| <CopyableCode code="net_buffer_length" /> | `integer` | Start sizes of connection buffer and result buffer, must be multiple of 1024. Changing this parameter will lead to a restart of the MySQL service. |
| <CopyableCode code="net_read_timeout" /> | `integer` | The time, in seconds, to wait for more data from an existing connection. aborting the read. |
| <CopyableCode code="net_write_timeout" /> | `integer` | The number of seconds to wait for a block to be written to a connection before aborting the write. |
| <CopyableCode code="num_partitions" /> | `integer` | Number of partitions for autocreated topics |
| <CopyableCode code="offsets_retention_minutes" /> | `integer` | Log retention window in minutes for offsets topic |
| <CopyableCode code="override_main_response_version" /> | `boolean` | Compatibility mode sets OpenSearch to report its version as 7.10 so clients continue to work. |
| <CopyableCode code="pg_partman_bgw.interval" /> | `integer` | Sets the time interval to run pg_partman's scheduled tasks. |
| <CopyableCode code="pg_partman_bgw.role" /> | `string` | Controls which role to use for pg_partman's scheduled background tasks. Must consist of alpha-numeric characters, dots, underscores, or dashes. May not start with dash or dot. Maximum of 64 characters. |
| <CopyableCode code="pg_stat_statements.track" /> | `string` | Controls which statements are counted. Specify 'top' to track top-level statements (those issued directly by clients), 'all' to also track nested statements (such as statements invoked within functions), or 'none' to disable statement statistics collection. The default value is top. |
| <CopyableCode code="pgbouncer" /> | `object` | PGBouncer connection pooling settings |
| <CopyableCode code="plugins_alerting_filter_by_backend_roles_enabled" /> | `boolean` | Enable or disable filtering of alerting by backend roles. |
| <CopyableCode code="producer_purgatory_purge_interval_requests" /> | `integer` | The purge interval (in number of requests) of the producer request purgatory (defaults to 1000). |
| <CopyableCode code="redis_acl_channels_default" /> | `string` | Determines default pub/sub channels' ACL for new users if ACL is not supplied. When this option is not defined, all_channels is assumed to keep backward compatibility. This option doesn't affect Redis configuration acl-pubsub-default. |
| <CopyableCode code="redis_io_threads" /> | `integer` | Redis IO thread count |
| <CopyableCode code="redis_lfu_decay_time" /> | `integer` | LFU maxmemory-policy counter decay time in minutes |
| <CopyableCode code="redis_lfu_log_factor" /> | `integer` | Counter logarithm factor for volatile-lfu and allkeys-lfu maxmemory-policies |
| <CopyableCode code="redis_maxmemory_policy" /> | `string` | A string specifying the desired eviction policy for the Redis cluster. - `noeviction`: Don't evict any data, returns error when memory limit is reached. - `allkeys_lru:` Evict any key, least recently used (LRU) first. - `allkeys_random`: Evict keys in a random order. - `volatile_lru`: Evict keys with expiration only, least recently used (LRU) first. - `volatile_random`: Evict keys with expiration only in a random order. - `volatile_ttl`: Evict keys with expiration only, shortest time-to-live (TTL) first. |
| <CopyableCode code="redis_notify_keyspace_events" /> | `string` | Set notify-keyspace-events option. Requires at least `K` or `E` and accepts any combination of the following options. Setting the parameter to `""` disables notifications. - `K` &mdash; Keyspace events - `E` &mdash; Keyevent events - `g` &mdash; Generic commands (e.g. `DEL`, `EXPIRE`, `RENAME`, ...) - `$` &mdash; String commands - `l` &mdash; List commands - `s` &mdash; Set commands - `h` &mdash; Hash commands - `z` &mdash; Sorted set commands - `t` &mdash; Stream commands - `d` &mdash; Module key type events - `x` &mdash; Expired events - `e` &mdash; Evicted events - `m` &mdash; Key miss events - `n` &mdash; New key events - `A` &mdash; Alias for `"g$lshztxed"` |
| <CopyableCode code="redis_number_of_databases" /> | `integer` | Set number of redis databases. Changing this will cause a restart of redis service. |
| <CopyableCode code="redis_persistence" /> | `string` | When persistence is 'rdb', Redis does RDB dumps each 10 minutes if any key is changed. Also RDB dumps are done according to backup schedule for backup purposes. When persistence is 'off', no RDB dumps and backups are done, so data can be lost at any moment if service is restarted for any reason, or if service is powered off. Also service can't be forked. |
| <CopyableCode code="redis_pubsub_client_output_buffer_limit" /> | `integer` | Set output buffer limit for pub / sub clients in MB. The value is the hard limit, the soft limit is 1/4 of the hard limit. When setting the limit, be mindful of the available memory in the selected service plan. |
| <CopyableCode code="redis_ssl" /> | `boolean` | Require SSL to access Redis. - When enabled, Redis accepts only SSL connections on port `25061`. - When disabled, port `25060` is opened for non-SSL connections, while port `25061` remains available for SSL connections. |
| <CopyableCode code="redis_timeout" /> | `integer` | Redis idle connection timeout in seconds |
| <CopyableCode code="reindex_remote_whitelist" /> | `array` | Allowlist of remote IP addresses for reindexing. Changing this value will cause all OpenSearch instances to restart. |
| <CopyableCode code="replica_fetch_max_bytes" /> | `integer` | The number of bytes of messages to attempt to fetch for each partition (defaults to 1048576). This is not an absolute maximum, if the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch will still be returned to ensure that progress can be made. |
| <CopyableCode code="replica_fetch_response_max_bytes" /> | `integer` | Maximum bytes expected for the entire fetch response (defaults to 10485760). Records are fetched in batches, and if the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch will still be returned to ensure that progress can be made. As such, this is not an absolute maximum. |
| <CopyableCode code="script_max_compilations_rate" /> | `string` | Limits the number of inline script compilations within a period of time. Default is use-context |
| <CopyableCode code="search_max_buckets" /> | `integer` | Maximum number of aggregation buckets allowed in a single response. |
| <CopyableCode code="shared_buffers_percentage" /> | `number` | Percentage of total RAM that the database server uses for shared memory buffers. Valid range is 20-60 (float), which corresponds to 20% - 60%. This setting adjusts the shared_buffers configuration value. |
| <CopyableCode code="slow_op_threshold_ms" /> | `integer` | Operations that run for longer than this threshold are considered slow which are then recorded to the diagnostic logs. Higher log levels (verbosity) will record all operations regardless of this threshold on the primary node. *Changing this parameter will lead to a restart of the MongoDB service.* Learn more [here](https://www.mongodb.com/docs/manual/reference/configuration-options/#mongodb-setting-operationProfiling.slowOpThresholdMs). |
| <CopyableCode code="slow_query_log" /> | `boolean` | When enabled, captures slow queries. When disabled, also truncates the mysql.slow_log table. Default is false. |
| <CopyableCode code="socket_request_max_bytes" /> | `integer` | The maximum number of bytes in a socket request (defaults to 104857600). |
| <CopyableCode code="sort_buffer_size" /> | `integer` | The sort buffer size, in bytes, for ORDER BY optimization. Default is 262144. (256K). |
| <CopyableCode code="sql_mode" /> | `string` | Global SQL mode. If empty, uses MySQL server defaults. Must only include uppercase alphabetic characters, underscores, and commas. |
| <CopyableCode code="sql_require_primary_key" /> | `boolean` | Require primary key to be defined for new tables or old tables modified with ALTER TABLE and fail if missing. It is recommended to always have primary keys because various functionality may break if any large table is missing them. |
| <CopyableCode code="stat_monitor_enable" /> | `boolean` | Enable the pg_stat_monitor extension. Enabling this extension will cause the cluster to be restarted. When this extension is enabled, pg_stat_statements results for utility commands are unreliable. |
| <CopyableCode code="synchronous_replication" /> | `string` | Synchronous replication type. Note that the service plan also needs to support synchronous replication. |
| <CopyableCode code="temp_file_limit" /> | `integer` | PostgreSQL temporary file limit in KiB. If -1, sets to unlimited. |
| <CopyableCode code="thread_pool_analyze_queue_size" /> | `integer` | Size of queue for operations in the analyze thread pool. |
| <CopyableCode code="thread_pool_analyze_size" /> | `integer` | Number of workers in the analyze operation thread pool. Do note this may have maximum value depending on CPU count - value is automatically lowered if set to higher than maximum value. |
| <CopyableCode code="thread_pool_force_merge_size" /> | `integer` | Number of workers in the force merge operation thread pool. This pool is used for forcing a merge between shards of one or more indices. Do note this may have maximum value depending on CPU count - value is automatically lowered if set to higher than maximum value. |
| <CopyableCode code="thread_pool_get_queue_size" /> | `integer` | Size of queue for operations in the get thread pool. |
| <CopyableCode code="thread_pool_get_size" /> | `integer` | Number of workers in the get operation thread pool. Do note this may have maximum value depending on CPU count - value is automatically lowered if set to higher than maximum value. |
| <CopyableCode code="thread_pool_search_queue_size" /> | `integer` | Size of queue for operations in the search thread pool. |
| <CopyableCode code="thread_pool_search_size" /> | `integer` | Number of workers in the search operation thread pool. Do note this may have maximum value depending on CPU count - value is automatically lowered if set to higher than maximum value. |
| <CopyableCode code="thread_pool_search_throttled_queue_size" /> | `integer` | Size of queue for operations in the search throttled thread pool. |
| <CopyableCode code="thread_pool_search_throttled_size" /> | `integer` | Number of workers in the search throttled operation thread pool. This pool is used for searching frozen indices. Do note this may have maximum value depending on CPU count - value is automatically lowered if set to higher than maximum value. |
| <CopyableCode code="thread_pool_write_queue_size" /> | `integer` | Size of queue for operations in the write thread pool. |
| <CopyableCode code="thread_pool_write_size" /> | `integer` | Number of workers in the write operation thread pool. Do note this may have maximum value depending on CPU count - value is automatically lowered if set to higher than maximum value. |
| <CopyableCode code="timescaledb" /> | `object` | TimescaleDB extension configuration values |
| <CopyableCode code="timezone" /> | `string` | PostgreSQL service timezone |
| <CopyableCode code="tmp_table_size" /> | `integer` | The maximum size, in bytes, of internal in-memory tables. Also set max_heap_table_size. Default is 16777216 (16M). |
| <CopyableCode code="track_activity_query_size" /> | `integer` | Specifies the number of bytes reserved to track the currently executing command for each active session. |
| <CopyableCode code="track_commit_timestamp" /> | `string` | Record commit time of transactions. |
| <CopyableCode code="track_functions" /> | `string` | Enables tracking of function call counts and time used. |
| <CopyableCode code="track_io_timing" /> | `string` | Enables timing of database I/O calls. This parameter is off by default, because it will repeatedly query the operating system for the current time, which may cause significant overhead on some platforms. |
| <CopyableCode code="transaction_lifetime_limit_seconds" /> | `integer` | Specifies the lifetime of multi-document transactions. Transactions that exceed this limit are considered expired and will be aborted by a periodic cleanup process. The cleanup process runs every `transactionLifetimeLimitSeconds/2 seconds` or at least once every 60 seconds. *Changing this parameter will lead to a restart of the MongoDB service.* Learn more [here](https://www.mongodb.com/docs/manual/reference/parameters/#mongodb-parameter-param.transactionLifetimeLimitSeconds). |
| <CopyableCode code="transaction_remove_expired_transaction_cleanup_interval_ms" /> | `integer` | The interval at which to remove transactions that have expired due to transactional.id.expiration.ms passing (defaults to 3600000 (1 hour)). |
| <CopyableCode code="transaction_state_log_segment_bytes" /> | `integer` | The transaction topic segment bytes should be kept relatively small in order to facilitate faster log compaction and cache loads (defaults to 104857600 (100 mebibytes)). |
| <CopyableCode code="verbosity" /> | `integer` | The log message verbosity level. The verbosity level determines the amount of Informational and Debug messages MongoDB outputs. 0 includes informational messages while 1...5 increases the level to include debug messages. *Changing this parameter will lead to a restart of the MongoDB service.* Learn more [here](https://www.mongodb.com/docs/manual/reference/configuration-options/#mongodb-setting-systemLog.verbosity). |
| <CopyableCode code="wait_timeout" /> | `integer` | The number of seconds the server waits for activity on a noninteractive connection before closing it. |
| <CopyableCode code="wal_sender_timeout" /> | `integer` | Terminate replication connections that are inactive for longer than this amount of time, in milliseconds. Setting this value to zero disables the timeout. Must be either 0 or between 5000 and 10800000. |
| <CopyableCode code="wal_writer_delay" /> | `integer` | WAL flush interval in milliseconds. Note that setting this value to lower than the default 200ms may negatively impact performance |
| <CopyableCode code="work_mem" /> | `integer` | The maximum amount of memory, in MB, used by a query operation (such as a sort or hash table) before writing to temporary disk files. Default is 1MB + 0.075% of total RAM (up to 32MB). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="databases_get_config" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | Shows configuration parameters for an existing database cluster by sending a GET request to `/v2/databases/$DATABASE_ID/config`. The response is a JSON object with a `config` key, which is set to an object containing any database configuration parameters. |
| <CopyableCode code="databases_patch_config" /> | `UPDATE` | <CopyableCode code="database_cluster_uuid" /> | To update the configuration for an existing database cluster, send a PATCH request to `/v2/databases/$DATABASE_ID/config`. |

## `SELECT` examples

Shows configuration parameters for an existing database cluster by sending a GET request to `/v2/databases/$DATABASE_ID/config`. The response is a JSON object with a `config` key, which is set to an object containing any database configuration parameters.


```sql
SELECT
_backup_hour,
_backup_minute,
action_auto_create_index_enabled,
action_destructive_requires_name,
auto_create_topics_enable,
autovacuum_analyze_scale_factor,
autovacuum_analyze_threshold,
autovacuum_freeze_max_age,
autovacuum_max_workers,
autovacuum_naptime,
autovacuum_vacuum_cost_delay,
autovacuum_vacuum_cost_limit,
autovacuum_vacuum_scale_factor,
autovacuum_vacuum_threshold,
backup_hour,
backup_minute,
bgwriter_delay,
bgwriter_flush_after,
bgwriter_lru_maxpages,
bgwriter_lru_multiplier,
binlog_retention_period,
cluster_max_shards_per_node,
cluster_routing_allocation_node_concurrent_recoveries,
compression_type,
connect_timeout,
connections_max_idle_ms,
deadlock_timeout,
default_read_concern,
default_replication_factor,
default_time_zone,
default_toast_compression,
default_write_concern,
enable_security_audit,
group_concat_max_len,
group_initial_rebalance_delay_ms,
group_max_session_timeout_ms,
group_min_session_timeout_ms,
http_max_content_length_bytes,
http_max_header_size_bytes,
http_max_initial_line_length_bytes,
idle_in_transaction_session_timeout,
indices_fielddata_cache_size_percentage,
indices_memory_index_buffer_size_percentage,
indices_memory_max_index_buffer_size_mb,
indices_memory_min_index_buffer_size_mb,
indices_queries_cache_size_percentage,
indices_query_bool_max_clause_count,
indices_recovery_max_concurrent_file_chunks,
indices_recovery_max_mb_per_sec,
information_schema_stats_expiry,
innodb_change_buffer_max_size,
innodb_flush_neighbors,
innodb_ft_min_token_size,
innodb_ft_server_stopword_table,
innodb_lock_wait_timeout,
innodb_log_buffer_size,
innodb_online_alter_log_max_size,
innodb_print_all_deadlocks,
innodb_read_io_threads,
innodb_rollback_on_timeout,
innodb_thread_concurrency,
innodb_write_io_threads,
interactive_timeout,
internal_tmp_mem_storage_engine,
ism_enabled,
ism_history_enabled,
ism_history_max_age_hours,
ism_history_max_docs,
ism_history_rollover_check_period_hours,
ism_history_rollover_retention_period_days,
jit,
log_autovacuum_min_duration,
log_cleaner_delete_retention_ms,
log_cleaner_max_compaction_lag_ms,
log_cleaner_min_cleanable_ratio,
log_cleaner_min_compaction_lag_ms,
log_cleanup_policy,
log_error_verbosity,
log_flush_interval_messages,
log_flush_interval_ms,
log_index_interval_bytes,
log_index_size_max_bytes,
log_line_prefix,
log_message_downconversion_enable,
log_message_timestamp_difference_max_ms,
log_message_timestamp_type,
log_min_duration_statement,
log_preallocate,
log_retention_bytes,
log_retention_hours,
log_retention_ms,
log_roll_jitter_ms,
log_roll_ms,
log_segment_bytes,
log_segment_delete_delay_ms,
long_query_time,
max_allowed_packet,
max_connections_per_ip,
max_failover_replication_time_lag,
max_files_per_process,
max_heap_table_size,
max_incremental_fetch_session_cache_slots,
max_locks_per_transaction,
max_logical_replication_workers,
max_parallel_workers,
max_parallel_workers_per_gather,
max_pred_locks_per_transaction,
max_prepared_transactions,
max_replication_slots,
max_stack_depth,
max_standby_archive_delay,
max_standby_streaming_delay,
max_wal_senders,
max_worker_processes,
message_max_bytes,
min_insync_replicas,
net_buffer_length,
net_read_timeout,
net_write_timeout,
num_partitions,
offsets_retention_minutes,
override_main_response_version,
pg_partman_bgw.interval,
pg_partman_bgw.role,
pg_stat_statements.track,
pgbouncer,
plugins_alerting_filter_by_backend_roles_enabled,
producer_purgatory_purge_interval_requests,
redis_acl_channels_default,
redis_io_threads,
redis_lfu_decay_time,
redis_lfu_log_factor,
redis_maxmemory_policy,
redis_notify_keyspace_events,
redis_number_of_databases,
redis_persistence,
redis_pubsub_client_output_buffer_limit,
redis_ssl,
redis_timeout,
reindex_remote_whitelist,
replica_fetch_max_bytes,
replica_fetch_response_max_bytes,
script_max_compilations_rate,
search_max_buckets,
shared_buffers_percentage,
slow_op_threshold_ms,
slow_query_log,
socket_request_max_bytes,
sort_buffer_size,
sql_mode,
sql_require_primary_key,
stat_monitor_enable,
synchronous_replication,
temp_file_limit,
thread_pool_analyze_queue_size,
thread_pool_analyze_size,
thread_pool_force_merge_size,
thread_pool_get_queue_size,
thread_pool_get_size,
thread_pool_search_queue_size,
thread_pool_search_size,
thread_pool_search_throttled_queue_size,
thread_pool_search_throttled_size,
thread_pool_write_queue_size,
thread_pool_write_size,
timescaledb,
timezone,
tmp_table_size,
track_activity_query_size,
track_commit_timestamp,
track_functions,
track_io_timing,
transaction_lifetime_limit_seconds,
transaction_remove_expired_transaction_cleanup_interval_ms,
transaction_state_log_segment_bytes,
verbosity,
wait_timeout,
wal_sender_timeout,
wal_writer_delay,
work_mem
FROM digitalocean.databases.configs
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}';
```
## `UPDATE` example

Updates a <code>configs</code> resource.

```sql
/*+ update */
UPDATE digitalocean.databases.configs
SET 
config = '{{ config }}'
WHERE 
database_cluster_uuid = '{{ database_cluster_uuid }}';
```

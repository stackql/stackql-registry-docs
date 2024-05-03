---
title: config
hide_title: false
hide_table_of_contents: false
keywords:
  - config
  - databases
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
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
| <CopyableCode code="backup_minute" /> | `integer` | The minute of the backup hour when backup for the service starts. New backup  only starts if previous backup has already completed. |
| <CopyableCode code="bgwriter_delay" /> | `integer` | Specifies the delay, in milliseconds, between activity rounds for the background writer. Default is 200 ms. |
| <CopyableCode code="bgwriter_flush_after" /> | `integer` | The amount of kilobytes that need to be written by the background writer before attempting to force the OS to issue these writes to underlying storage. Specified in kilobytes, default is 512.  Setting of 0 disables forced writeback. |
| <CopyableCode code="bgwriter_lru_maxpages" /> | `integer` | The maximum number of buffers that the background writer can write. Setting this to zero disables background writing. Default is 100. |
| <CopyableCode code="bgwriter_lru_multiplier" /> | `number` | The average recent need for new buffers is multiplied by bgwriter_lru_multiplier to arrive at an estimate of the number that will be needed during the next round, (up to bgwriter_lru_maxpages). 1.0 represents a “just in time” policy of writing exactly the number of buffers predicted to be needed. Larger values provide some cushion against spikes in demand, while smaller values intentionally leave writes to be done by server processes. The default is 2.0. |
| <CopyableCode code="binlog_retention_period" /> | `number` | The minimum amount of time, in seconds, to keep binlog entries before deletion.  This may be extended for services that require binlog entries for longer than the default, for example if using the MySQL Debezium Kafka connector. |
| <CopyableCode code="connect_timeout" /> | `integer` | The number of seconds that the mysqld server waits for a connect packet before responding with bad handshake. |
| <CopyableCode code="deadlock_timeout" /> | `integer` | The amount of time, in milliseconds, to wait on a lock before checking to see if there is a deadlock condition. |
| <CopyableCode code="default_time_zone" /> | `string` | Default server time zone, in the form of an offset from UTC (from -12:00 to +12:00), a time zone name (EST), or 'SYSTEM' to use the MySQL server default. |
| <CopyableCode code="default_toast_compression" /> | `string` | Specifies the default TOAST compression method for values of compressible columns (the default is lz4). |
| <CopyableCode code="group_concat_max_len" /> | `integer` | The maximum permitted result length, in bytes, for the GROUP_CONCAT() function. |
| <CopyableCode code="idle_in_transaction_session_timeout" /> | `integer` | Time out sessions with open transactions after this number of milliseconds |
| <CopyableCode code="information_schema_stats_expiry" /> | `integer` | The time, in seconds, before cached statistics expire. |
| <CopyableCode code="innodb_ft_min_token_size" /> | `integer` | The minimum length of words that an InnoDB FULLTEXT index stores. |
| <CopyableCode code="innodb_ft_server_stopword_table" /> | `string` | The InnoDB FULLTEXT index stopword list for all InnoDB tables. |
| <CopyableCode code="innodb_lock_wait_timeout" /> | `integer` | The time, in seconds, that an InnoDB transaction waits for a row lock. before giving up. |
| <CopyableCode code="innodb_log_buffer_size" /> | `integer` | The size of the buffer, in bytes, that InnoDB uses to write to the log files. on disk. |
| <CopyableCode code="innodb_online_alter_log_max_size" /> | `integer` | The upper limit, in bytes, of the size of the temporary log files used during online DDL operations for InnoDB tables. |
| <CopyableCode code="innodb_print_all_deadlocks" /> | `boolean` | When enabled, records information about all deadlocks in InnoDB user transactions  in the error log. Disabled by default. |
| <CopyableCode code="innodb_rollback_on_timeout" /> | `boolean` | When enabled, transaction timeouts cause InnoDB to abort and roll back the entire transaction. |
| <CopyableCode code="interactive_timeout" /> | `integer` | The time, in seconds, the server waits for activity on an interactive. connection before closing it. |
| <CopyableCode code="internal_tmp_mem_storage_engine" /> | `string` | The storage engine for in-memory internal temporary tables. |
| <CopyableCode code="jit" /> | `boolean` | Activates, in a boolean, the system-wide use of Just-in-Time Compilation (JIT). |
| <CopyableCode code="log_autovacuum_min_duration" /> | `integer` | Causes each action executed by autovacuum to be logged if it ran for at least the specified number of milliseconds. Setting this to zero logs all autovacuum actions. Minus-one (the default) disables logging autovacuum actions. |
| <CopyableCode code="log_error_verbosity" /> | `string` | Controls the amount of detail written in the server log for each message that is logged. |
| <CopyableCode code="log_line_prefix" /> | `string` | Selects one of the available log-formats. These can support popular log analyzers like pgbadger, pganalyze, etc. |
| <CopyableCode code="log_min_duration_statement" /> | `integer` | Log statements that take more than this number of milliseconds to run. If -1, disables. |
| <CopyableCode code="long_query_time" /> | `number` | The time, in seconds, for a query to take to execute before  being captured by slow_query_logs. Default is 10 seconds. |
| <CopyableCode code="max_allowed_packet" /> | `integer` | The size of the largest message, in bytes, that can be received by the server. Default is 67108864 (64M). |
| <CopyableCode code="max_files_per_process" /> | `integer` | PostgreSQL maximum number of files that can be open per process. |
| <CopyableCode code="max_heap_table_size" /> | `integer` | The maximum size, in bytes, of internal in-memory tables. Also set tmp_table_size. Default is 16777216 (16M) |
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
| <CopyableCode code="net_read_timeout" /> | `integer` | The time, in seconds, to wait for more data from an existing connection. aborting the read. |
| <CopyableCode code="net_write_timeout" /> | `integer` | The number of seconds to wait for a block to be written to a connection before aborting the write. |
| <CopyableCode code="pg_partman_bgw.interval" /> | `integer` | Sets the time interval to run pg_partman's scheduled tasks. |
| <CopyableCode code="pg_partman_bgw.role" /> | `string` | Controls which role to use for pg_partman's scheduled background tasks. Must consist of alpha-numeric characters, dots, underscores, or dashes. May not start with dash or dot. Maximum of 64 characters. |
| <CopyableCode code="pg_stat_statements.track" /> | `string` | Controls which statements are counted. Specify 'top' to track top-level statements (those issued directly by clients), 'all' to also track nested statements (such as statements invoked within functions), or 'none' to disable statement statistics collection. The default value is top. |
| <CopyableCode code="pgbouncer" /> | `object` | PGBouncer connection pooling settings |
| <CopyableCode code="postgres_backup_hour" /> | `integer` | The hour of day (in UTC) when backup for the service starts. New backup only starts if previous backup has already completed. |
| <CopyableCode code="postgres_backup_minute" /> | `integer` | The minute of the backup hour when backup for the service starts. New backup is only started if previous backup has already completed. |
| <CopyableCode code="redis_acl_channels_default" /> | `string` | Determines default pub/sub channels' ACL for new users if ACL is not supplied. When this option is not defined, all_channels is assumed to keep backward compatibility. This option doesn't affect Redis configuration acl-pubsub-default. |
| <CopyableCode code="redis_io_threads" /> | `integer` | Redis IO thread count |
| <CopyableCode code="redis_lfu_decay_time" /> | `integer` | LFU maxmemory-policy counter decay time in minutes |
| <CopyableCode code="redis_lfu_log_factor" /> | `integer` | Counter logarithm factor for volatile-lfu and allkeys-lfu maxmemory-policies |
| <CopyableCode code="redis_maxmemory_policy" /> | `string` | A string specifying the desired eviction policy for the Redis cluster.<br /><br />- `noeviction`: Don't evict any data, returns error when memory limit is reached.<br />- `allkeys_lru:` Evict any key, least recently used (LRU) first.<br />- `allkeys_random`: Evict keys in a random order.<br />- `volatile_lru`: Evict keys with expiration only, least recently used (LRU) first.<br />- `volatile_random`: Evict keys with expiration only in a random order.<br />- `volatile_ttl`: Evict keys with expiration only, shortest time-to-live (TTL) first. |
| <CopyableCode code="redis_notify_keyspace_events" /> | `string` | Set notify-keyspace-events option |
| <CopyableCode code="redis_number_of_databases" /> | `integer` | Set number of redis databases. Changing this will cause a restart of redis service. |
| <CopyableCode code="redis_persistence" /> | `string` | When persistence is 'rdb', Redis does RDB dumps each 10 minutes if any key is changed. Also RDB dumps are done according to backup schedule for backup purposes. When persistence is 'off', no RDB dumps and backups are done, so data can be lost at any moment if service is restarted for any reason, or if service is powered off. Also service can't be forked. |
| <CopyableCode code="redis_pubsub_client_output_buffer_limit" /> | `integer` | Set output buffer limit for pub / sub clients in MB. The value is the hard limit, the soft limit is 1/4 of the hard limit. When setting the limit, be mindful of the available memory in the selected service plan. |
| <CopyableCode code="redis_ssl" /> | `boolean` | Require SSL to access Redis |
| <CopyableCode code="redis_timeout" /> | `integer` | Redis idle connection timeout in seconds |
| <CopyableCode code="shared_buffers_percentage" /> | `number` | Percentage of total RAM that the database server uses for shared memory buffers.  Valid range is 20-60 (float), which corresponds to 20% - 60%.  This setting adjusts the shared_buffers configuration value. |
| <CopyableCode code="slow_query_log" /> | `boolean` | When enabled, captures slow queries. When disabled, also truncates the mysql.slow_log table. Default is false. |
| <CopyableCode code="sort_buffer_size" /> | `integer` | The sort buffer size, in bytes, for ORDER BY optimization. Default is 262144. (256K). |
| <CopyableCode code="sql_mode" /> | `string` | Global SQL mode. If empty, uses MySQL server defaults. Must only include uppercase alphabetic characters, underscores, and commas. |
| <CopyableCode code="sql_require_primary_key" /> | `boolean` | Require primary key to be defined for new tables or old tables modified with ALTER TABLE and fail if missing. It is recommended to always have primary keys because various functionality may break if any large table is missing them. |
| <CopyableCode code="stat_monitor_enable" /> | `boolean` | Enable the pg_stat_monitor extension. &lt;b&gt;Enabling this extension will cause the cluster to be restarted.&lt;/b&gt; When this extension is enabled, pg_stat_statements results for utility commands are unreliable. |
| <CopyableCode code="synchronous_replication" /> | `string` | Synchronous replication type. Note that the service plan also needs to support synchronous replication. |
| <CopyableCode code="temp_file_limit" /> | `integer` | PostgreSQL temporary file limit in KiB. If -1, sets to unlimited. |
| <CopyableCode code="timescaledb" /> | `object` | TimescaleDB extension configuration values |
| <CopyableCode code="timezone" /> | `string` | PostgreSQL service timezone |
| <CopyableCode code="tmp_table_size" /> | `integer` | The maximum size, in bytes, of internal in-memory tables. Also set max_heap_table_size. Default is 16777216 (16M). |
| <CopyableCode code="track_activity_query_size" /> | `integer` | Specifies the number of bytes reserved to track the currently executing command for each active session. |
| <CopyableCode code="track_commit_timestamp" /> | `string` | Record commit time of transactions. |
| <CopyableCode code="track_functions" /> | `string` | Enables tracking of function call counts and time used. |
| <CopyableCode code="track_io_timing" /> | `string` | Enables timing of database I/O calls. This parameter is off by default, because it will repeatedly query the operating system for the current time, which may cause significant overhead on some platforms. |
| <CopyableCode code="wait_timeout" /> | `integer` | The number of seconds the server waits for activity on a noninteractive connection before closing it. |
| <CopyableCode code="wal_sender_timeout" /> | `integer` | Terminate replication connections that are inactive for longer than this amount of time, in milliseconds. Setting this value to zero disables the timeout. Must be either 0 or between 5000 and 10800000. |
| <CopyableCode code="wal_writer_delay" /> | `integer` | WAL flush interval in milliseconds. Note that setting this value to lower than the default 200ms may negatively impact performance |
| <CopyableCode code="work_mem" /> | `integer` | The maximum amount of memory, in MB, used by a query operation (such as a sort or hash table) before writing to temporary disk files. Default is 1MB + 0.075% of total RAM (up to 32MB). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_config" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | Shows configuration parameters for an existing database cluster by sending a GET request to<br />`/v2/databases/$DATABASE_ID/config`.<br />The response is a JSON object with a `config` key, which is set to an object<br />containing any database configuration parameters.<br /> |
| <CopyableCode code="_get_config" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> | Shows configuration parameters for an existing database cluster by sending a GET request to<br />`/v2/databases/$DATABASE_ID/config`.<br />The response is a JSON object with a `config` key, which is set to an object<br />containing any database configuration parameters.<br /> |
| <CopyableCode code="patch_config" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> | To update the configuration for an existing database cluster, send a PATCH request to<br />`/v2/databases/$DATABASE_ID/config`.<br /> |

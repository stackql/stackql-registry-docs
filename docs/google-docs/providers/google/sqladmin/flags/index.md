---
title: flags
hide_title: false
hide_table_of_contents: false
keywords:
  - flags
  - sqladmin
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sqladmin.flags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | This is the name of the flag. Flag names always use underscores, not hyphens, for example: `max_allowed_packet` |
| <CopyableCode code="allowedIntValues" /> | `array` | Use this field if only certain integers are accepted. Can be combined with min_value and max_value to add additional values. |
| <CopyableCode code="allowedStringValues" /> | `array` | For `STRING` flags, a list of strings that the value can be set to. |
| <CopyableCode code="appliesTo" /> | `array` | The database version this flag applies to. Can be MySQL instances: `MYSQL_8_0`, `MYSQL_8_0_18`, `MYSQL_8_0_26`, `MYSQL_5_7`, or `MYSQL_5_6`. PostgreSQL instances: `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11` or `POSTGRES_12`. SQL Server instances: `SQLSERVER_2017_STANDARD`, `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`, `SQLSERVER_2019_STANDARD`, `SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`, or `SQLSERVER_2019_WEB`. See [the complete list](/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion). |
| <CopyableCode code="inBeta" /> | `boolean` | Whether or not the flag is considered in beta. |
| <CopyableCode code="kind" /> | `string` | This is always `sql#flag`. |
| <CopyableCode code="maxValue" /> | `string` | For `INTEGER` flags, the maximum allowed value. |
| <CopyableCode code="minValue" /> | `string` | For `INTEGER` flags, the minimum allowed value. |
| <CopyableCode code="requiresRestart" /> | `boolean` | Indicates whether changing this flag will trigger a database restart. Only applicable to Second Generation instances. |
| <CopyableCode code="type" /> | `string` | The type of the flag. Flags are typed to being `BOOLEAN`, `STRING`, `INTEGER` or `NONE`. `NONE` is used for flags that do not take a value, such as `skip_grant_tables`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |

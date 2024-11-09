---
title: statement_exceptions
hide_title: false
hide_table_of_contents: false
keywords:
  - statement_exceptions
  - sql
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>statement_exceptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>statement_exceptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.sql.statement_exceptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the SQL statement exception. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="message" /> | `string` | Error message of the statement exception. |
| <CopyableCode code="timestamp" /> | `string` | The date and time at which the exception occurred. It is represented in RFC3339 format and is in UTC. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_sqlv1statement_exceptions" /> | `SELECT` | <CopyableCode code="environment_id, organization_id, statement_name" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a list of the 10 most recent statement exceptions. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a list of the 10 most recent statement exceptions.


```sql
SELECT
name,
kind,
message,
timestamp
FROM confluent.sql.statement_exceptions
WHERE environment_id = '{{ environment_id }}'
AND organization_id = '{{ organization_id }}'
AND statement_name = '{{ statement_name }}';
```
---
title: statement_results
hide_title: false
hide_table_of_contents: false
keywords:
  - statement_results
  - sql
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>statement_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>statement_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.sql.statement_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="_results" /> | `object` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `object` | ListMeta describes metadata that resource collections may have |
| <CopyableCode code="results" /> | `object` | A results property that contains a data property that contains an array of results. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_sqlv1statement_result" /> | `SELECT` | <CopyableCode code="environment_id, name, organization_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Read Statement Result. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Read Statement Result.


```sql
SELECT
_results,
api_version,
kind,
metadata,
results
FROM confluent.sql.statement_results
WHERE environment_id = '{{ environment_id }}'
AND name = '{{ name }}'
AND organization_id = '{{ organization_id }}';
```
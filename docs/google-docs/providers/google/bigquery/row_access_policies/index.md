---
title: row_access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - row_access_policies
  - bigquery
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>row_access_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>row_access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigquery.row_access_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creationTime" /> | `string` | Output only. The time when this row access policy was created, in milliseconds since the epoch. |
| <CopyableCode code="etag" /> | `string` | Output only. A hash of this resource. |
| <CopyableCode code="filterPredicate" /> | `string` | Required. A SQL boolean expression that represents the rows defined by this row access policy, similar to the boolean expression in a WHERE clause of a SELECT query on a table. References to other tables, routines, and temporary functions are not supported. Examples: region="EU" date_field = CAST('2019-9-27' as DATE) nullable_field is not NULL numeric_field BETWEEN 1.0 AND 5.0 |
| <CopyableCode code="lastModifiedTime" /> | `string` | Output only. The time when this row access policy was last modified, in milliseconds since the epoch. |
| <CopyableCode code="rowAccessPolicyReference" /> | `object` | Id path of a row access policy. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="+datasetId, +tableId, projectId" /> | Lists all row access policies on the specified table. |

## `SELECT` examples

Lists all row access policies on the specified table.

```sql
SELECT
creationTime,
etag,
filterPredicate,
lastModifiedTime,
rowAccessPolicyReference
FROM google.bigquery.row_access_policies
WHERE +datasetId = '{{ +datasetId }}'
AND +tableId = '{{ +tableId }}'
AND projectId = '{{ projectId }}';
```

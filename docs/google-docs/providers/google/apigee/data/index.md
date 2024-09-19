---
title: data
hide_title: false
hide_table_of_contents: false
keywords:
  - data
  - apigee
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

Creates, updates, deletes, gets or lists a <code>data</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.data" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="completed" /> | `boolean` | Flag indicating whether a transaction is completed or not |
| <CopyableCode code="point" /> | `array` | List of debug data collected by runtime plane at various defined points in the flow. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_apis_revisions_debugsessions_data_get" /> | `SELECT` | <CopyableCode code="apisId, dataId, debugsessionsId, environmentsId, organizationsId, revisionsId" /> | Gets the debug data from a transaction. |

## `SELECT` examples

Gets the debug data from a transaction.

```sql
SELECT
completed,
point
FROM google.apigee.data
WHERE apisId = '{{ apisId }}'
AND dataId = '{{ dataId }}'
AND debugsessionsId = '{{ debugsessionsId }}'
AND environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'
AND revisionsId = '{{ revisionsId }}';
```

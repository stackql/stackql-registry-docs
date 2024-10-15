---
title: alerts_enrichments
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_enrichments
  - alerts_management
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

Creates, updates, deletes, gets or lists a <code>alerts_enrichments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts_enrichments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.alerts_management.alerts_enrichments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="properties" /> | `object` | Properties of the alert enrichment item. |
| <CopyableCode code="type" /> | `string` | Azure resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertId, scope" /> | Get the enrichments of an alert. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="alertId, scope" /> | List the enrichments of an alert. It returns a collection of one object named default. |

## `SELECT` examples

Get the enrichments of an alert.


```sql
SELECT
id,
name,
properties,
type
FROM azure.alerts_management.alerts_enrichments
WHERE alertId = '{{ alertId }}'
AND scope = '{{ scope }}';
```
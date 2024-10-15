---
title: deleted_workbooks
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_workbooks
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>deleted_workbooks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deleted_workbooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.deleted_workbooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource etag |
| <CopyableCode code="kind" /> | `string` | The kind of workbook. Only valid value is shared. |
| <CopyableCode code="properties" /> | `object` | Properties that contain a workbook. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all recently deleted Workbooks in a specified subscription. |

## `SELECT` examples

Get all recently deleted Workbooks in a specified subscription.


```sql
SELECT
etag,
kind,
properties,
systemData
FROM azure.application_insights.deleted_workbooks
WHERE subscriptionId = '{{ subscriptionId }}';
```
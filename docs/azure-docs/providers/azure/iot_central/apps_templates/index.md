---
title: apps_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - apps_templates
  - iot_central
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

Creates, updates, deletes, gets or lists a <code>apps_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_central.apps_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the template. |
| <CopyableCode code="description" /> | `string` | The description of the template. |
| <CopyableCode code="industry" /> | `string` | The industry of the template. |
| <CopyableCode code="locations" /> | `array` | A list of locations that support the template. |
| <CopyableCode code="manifestId" /> | `string` | The ID of the template. |
| <CopyableCode code="manifestVersion" /> | `string` | The version of the template. |
| <CopyableCode code="order" /> | `number` | The order of the template in the templates list. |
| <CopyableCode code="title" /> | `string` | The title of the template. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all available application templates. |

## `SELECT` examples

Get all available application templates.


```sql
SELECT
name,
description,
industry,
locations,
manifestId,
manifestVersion,
order,
title
FROM azure.iot_central.apps_templates
WHERE subscriptionId = '{{ subscriptionId }}';
```
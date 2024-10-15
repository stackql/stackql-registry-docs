---
title: service_fabrics_applicable_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - service_fabrics_applicable_schedules
  - dev_test_labs
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

Creates, updates, deletes, gets or lists a <code>service_fabrics_applicable_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_fabrics_applicable_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.service_fabrics_applicable_schedules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a schedules applicable to a virtual machine. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, userName" /> | Lists the applicable start/stop schedules, if any. |

## `SELECT` examples

Lists the applicable start/stop schedules, if any.


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.dev_test_labs.service_fabrics_applicable_schedules
WHERE labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userName = '{{ userName }}';
```
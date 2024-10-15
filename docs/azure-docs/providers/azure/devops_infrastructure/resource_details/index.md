---
title: resource_details
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_details
  - devops_infrastructure
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

Creates, updates, deletes, gets or lists a <code>resource_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.devops_infrastructure.resource_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Details of the ResourceDetailsObject. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_pool" /> | `SELECT` | <CopyableCode code="poolName, resourceGroupName, subscriptionId" /> | List ResourceDetailsObject resources by Pool |

## `SELECT` examples

List ResourceDetailsObject resources by Pool


```sql
SELECT
properties
FROM azure.devops_infrastructure.resource_details
WHERE poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
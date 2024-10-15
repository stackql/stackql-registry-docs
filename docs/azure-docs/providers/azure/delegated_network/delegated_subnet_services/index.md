---
title: delegated_subnet_services
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_subnet_services
  - delegated_network
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

Creates, updates, deletes, gets or lists a <code>delegated_subnet_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delegated_subnet_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.delegated_network.delegated_subnet_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of delegated subnet |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The type of resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the DelegatedSubnets resources in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all the DelegatedSubnets resources in a subscription. |
| <CopyableCode code="patch_details" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Patch delegated subnet resource |
| <CopyableCode code="put_details" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Put delegated subnet resource |

## `SELECT` examples

Get all the DelegatedSubnets resources in a subscription.


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.delegated_network.delegated_subnet_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
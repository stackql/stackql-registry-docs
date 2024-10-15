---
title: azure_firewall_fqdn_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_firewall_fqdn_tags
  - network
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

Creates, updates, deletes, gets or lists a <code>azure_firewall_fqdn_tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure_firewall_fqdn_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.azure_firewall_fqdn_tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Azure Firewall FQDN Tag Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the Azure Firewall FQDN Tags in a subscription. |

## `SELECT` examples

Gets all the Azure Firewall FQDN Tags in a subscription.


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.network.azure_firewall_fqdn_tags
WHERE subscriptionId = '{{ subscriptionId }}';
```
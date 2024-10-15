---
title: virtual_machine_images_edge_zone_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_images_edge_zone_skus
  - compute
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_images_edge_zone_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_images_edge_zone_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_images_edge_zone_skus" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="edgeZone, location, offer, publisherName, subscriptionId" /> | Gets a list of virtual machine image SKUs for the specified location, edge zone, publisher, and offer. |

## `SELECT` examples

Gets a list of virtual machine image SKUs for the specified location, edge zone, publisher, and offer.


```sql
SELECT

FROM azure.compute.virtual_machine_images_edge_zone_skus
WHERE edgeZone = '{{ edgeZone }}'
AND location = '{{ location }}'
AND offer = '{{ offer }}'
AND publisherName = '{{ publisherName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
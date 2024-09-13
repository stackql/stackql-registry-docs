---
title: networks_consumer_config
hide_title: false
hide_table_of_contents: false
keywords:
  - networks_consumer_config
  - servicenetworking
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

Creates, updates, deletes or gets an <code>networks_consumer_config</code> resource or lists <code>networks_consumer_config</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks_consumer_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicenetworking.networks_consumer_config" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update_consumer_config" /> | `UPDATE` | <CopyableCode code="networksId, projectsId, servicesId" /> | Service producers use this method to update the configuration of their connection including the import/export of custom routes and subnetwork routes with public IP. |

## `UPDATE` example

Updates a networks_consumer_config only if the necessary resources are available.

```sql
UPDATE google.servicenetworking.networks_consumer_config
SET 
consumerConfig = '{{ consumerConfig }}'
WHERE 
networksId = '{{ networksId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```

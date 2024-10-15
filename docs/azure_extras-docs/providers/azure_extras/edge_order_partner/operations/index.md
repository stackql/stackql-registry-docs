---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - edge_order_partner
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

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edge_order_partner.operations" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="manage_inventory_metadata" /> | `EXEC` | <CopyableCode code="familyIdentifier, location, serialNumber, subscriptionId, data__inventoryMetadata" /> |  |
| <CopyableCode code="manage_link" /> | `EXEC` | <CopyableCode code="familyIdentifier, location, serialNumber, subscriptionId, data__managementResourceArmId, data__operation, data__tenantId" /> |  |
| <CopyableCode code="search_inventories" /> | `EXEC` | <CopyableCode code="subscriptionId, data__familyIdentifier, data__serialNumber" /> |  |

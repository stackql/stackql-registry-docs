---
title: offers
hide_title: false
hide_table_of_contents: false
keywords:
  - offers
  - azure_stack_hci
  - azure_stack    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.offers" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, offerName, publisherName, resourceGroupName, subscriptionId" /> | Get Offer resource details within a publisher of HCI Cluster. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List Offers available across publishers for the HCI Cluster. |
| <CopyableCode code="list_by_publisher" /> | `SELECT` | <CopyableCode code="clusterName, publisherName, resourceGroupName, subscriptionId" /> | List Offers available for a publisher within the HCI Cluster. |
| <CopyableCode code="_list_by_cluster" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List Offers available across publishers for the HCI Cluster. |
| <CopyableCode code="_list_by_publisher" /> | `EXEC` | <CopyableCode code="clusterName, publisherName, resourceGroupName, subscriptionId" /> | List Offers available for a publisher within the HCI Cluster. |

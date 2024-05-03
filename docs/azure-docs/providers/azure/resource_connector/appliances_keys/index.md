---
title: appliances_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - appliances_keys
  - resource_connector
  - azure    
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
<tr><td><b>Name</b></td><td><code>appliances_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_connector.appliances_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="artifactProfiles" /> | `object` | Map of artifacts that contains a list of ArtifactProfile used to upload artifacts such as logs. |
| <CopyableCode code="kubeconfigs" /> | `array` | The list of appliance kubeconfigs. |
| <CopyableCode code="sshKeys" /> | `object` | Map of Customer User Public, Private SSH Keys and Certificate when available. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |

---
title: extension_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - extension_metadata
  - hybrid_compute
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
<tr><td><b>Name</b></td><td><code>extension_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.extension_metadata" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="extensionType, location, publisher, subscriptionId, version" /> | Gets an Extension Metadata based on location, publisher, extensionType and version |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="extensionType, location, publisher, subscriptionId" /> | Gets all Extension versions based on location, publisher, extensionType |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="extensionType, location, publisher, subscriptionId" /> | Gets all Extension versions based on location, publisher, extensionType |

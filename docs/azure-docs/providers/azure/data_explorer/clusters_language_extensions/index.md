---
title: clusters_language_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_language_extensions
  - data_explorer
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
<tr><td><b>Name</b></td><td><code>clusters_language_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.clusters_language_extensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="languageExtensionCustomImageName" /> | `string` | The sandbox custom image name that should be enabled as the active language extension. Sandbox custom image is a cluster sub resource. When this property is set, LanguageExtensionImageName should be set to 'PythonCustomImage'. |
| <CopyableCode code="languageExtensionImageName" /> | `string` | Language extension image name. |
| <CopyableCode code="languageExtensionName" /> | `string` | Language extension that can run within KQL query. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> |

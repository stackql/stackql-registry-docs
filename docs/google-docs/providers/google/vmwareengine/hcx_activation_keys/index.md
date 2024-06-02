---
title: hcx_activation_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - hcx_activation_keys
  - vmwareengine
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hcx_activation_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vmwareengine.hcx_activation_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this HcxActivationKey. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1/privateClouds/my-cloud/hcxActivationKeys/my-key` |
| <CopyableCode code="activationKey" /> | `string` | Output only. HCX activation key. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of HCX activation key. |
| <CopyableCode code="state" /> | `string` | Output only. State of HCX activation key. |
| <CopyableCode code="uid" /> | `string` | Output only. System-generated unique identifier for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hcxActivationKeysId, locationsId, privateCloudsId, projectsId" /> | Retrieves a `HcxActivationKey` resource by its resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Lists `HcxActivationKey` resources in a given private cloud. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Creates a new HCX activation key in a given private cloud. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Lists `HcxActivationKey` resources in a given private cloud. |

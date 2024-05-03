---
title: admissionregistration_v1
hide_title: false
hide_table_of_contents: false
keywords:
  - admissionregistration_v1
  - admissionregistration_v1
  - k8s    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Kubernetes resources using SQL
custom_edit_url: null
image: /img/providers/k8s/stackql-k8s-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>admissionregistration_v1</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.admissionregistration_v1.admissionregistration_v1" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiVersion" /> | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| <CopyableCode code="groupVersion" /> | `string` | groupVersion is the group and version this APIResourceList is for. |
| <CopyableCode code="kind" /> | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| <CopyableCode code="resources" /> | `array` | resources contains the name of the resources and if they are namespaced. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getAdmissionregistrationV1APIResources" /> | `SELECT` | <CopyableCode code="cluster_addr, protocol" /> |

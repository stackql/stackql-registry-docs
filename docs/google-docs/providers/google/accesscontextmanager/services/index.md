---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - accesscontextmanager
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.accesscontextmanager.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The service name or address of the supported service, such as `service.googleapis.com`. |
| <CopyableCode code="availableOnRestrictedVip" /> | `boolean` | True if the service is available on the restricted VIP. Services on the restricted VIP typically either support VPC Service Controls or are core infrastructure services required for the functioning of Google Cloud. |
| <CopyableCode code="knownLimitations" /> | `boolean` | True if the service is supported with some limitations. Check [documentation](https://cloud.google.com/vpc-service-controls/docs/supported-products) for details. |
| <CopyableCode code="supportStage" /> | `string` | The support stage of the service. |
| <CopyableCode code="supportedMethods" /> | `array` | The list of the supported methods. This field exists only in response to GetSupportedService |
| <CopyableCode code="title" /> | `string` | The name of the supported product, such as 'Cloud Product API'. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name" /> | Returns a VPC-SC supported service based on the service name. |
| <CopyableCode code="list" /> | `SELECT` |  | Lists all VPC-SC supported services. |
| <CopyableCode code="_list" /> | `EXEC` |  | Lists all VPC-SC supported services. |

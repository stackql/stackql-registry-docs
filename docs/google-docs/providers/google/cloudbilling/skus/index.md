---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - cloudbilling
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
<tr><td><b>Name</b></td><td><code>skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudbilling.skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name for the SKU. Example: "services/DA34-426B-A397/skus/AA95-CD31-42FE" |
| <CopyableCode code="description" /> | `string` | A human readable description of the SKU, has a maximum length of 256 characters. |
| <CopyableCode code="category" /> | `object` | Represents the category hierarchy of a SKU. |
| <CopyableCode code="geoTaxonomy" /> | `object` | Encapsulates the geographic taxonomy data for a sku. |
| <CopyableCode code="pricingInfo" /> | `array` | A timeline of pricing info for this SKU in chronological order. |
| <CopyableCode code="serviceProviderName" /> | `string` | Identifies the service provider. This is 'Google' for first party services in Google Cloud Platform. |
| <CopyableCode code="serviceRegions" /> | `array` | List of service regions this SKU is offered at. Example: "asia-east1" Service regions can be found at https://cloud.google.com/about/locations/ |
| <CopyableCode code="skuId" /> | `string` | The identifier for the SKU. Example: "AA95-CD31-42FE" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="servicesId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="servicesId" /> |

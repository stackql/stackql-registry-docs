---
title: mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - mappings
  - profilemapping
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.profilemapping.mappings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="properties" /> | `object` |
| <CopyableCode code="source" /> | `object` |
| <CopyableCode code="target" /> | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mappingId, subdomain" /> | Fetches a single Profile Mapping referenced by its ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> | Enumerates Profile Mappings in your organization with pagination. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="mappingId, subdomain" /> | Updates an existing Profile Mapping by adding, updating, or removing one or many Property Mappings. |

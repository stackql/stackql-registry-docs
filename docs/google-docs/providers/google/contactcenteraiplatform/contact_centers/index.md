---
title: contact_centers
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_centers
  - contactcenteraiplatform
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
<tr><td><b>Name</b></td><td><code>contact_centers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenteraiplatform.contact_centers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | name of resource |
| <CopyableCode code="adminUser" /> | `object` | Message storing info about the first admin user. Next ID: 3 |
| <CopyableCode code="ccaipManagedUsers" /> | `boolean` | Optional. Whether to enable users to be created in the CCAIP-instance concurrently to having users in Cloud identity |
| <CopyableCode code="createTime" /> | `string` | Output only. [Output only] Create time stamp |
| <CopyableCode code="customerDomainPrefix" /> | `string` | Required. Immutable. At least 2 and max 16 char long, must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). |
| <CopyableCode code="displayName" /> | `string` | Required. A user friendly name for the ContactCenter. |
| <CopyableCode code="instanceConfig" /> | `object` | Message storing the instance configuration. |
| <CopyableCode code="kmsKey" /> | `string` | Immutable. The KMS key name to encrypt the user input (`ContactCenter`). |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs |
| <CopyableCode code="samlParams" /> | `object` | Message storing SAML params to enable Google as IDP. |
| <CopyableCode code="state" /> | `string` | Output only. The state of this contact center. |
| <CopyableCode code="updateTime" /> | `string` | Output only. [Output only] Update time stamp |
| <CopyableCode code="uris" /> | `object` | Message storing the URIs of the ContactCenter. |
| <CopyableCode code="userEmail" /> | `string` | Optional. Email address of the first admin user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="contactCentersId, locationsId, projectsId" /> | Gets details of a single ContactCenter. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ContactCenters in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ContactCenter in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="contactCentersId, locationsId, projectsId" /> | Deletes a single ContactCenter. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists ContactCenters in a given project and location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="contactCentersId, locationsId, projectsId" /> | Updates the parameters of a single ContactCenter. |

---
title: deployed_ingress_config
hide_title: false
hide_table_of_contents: false
keywords:
  - deployed_ingress_config
  - apigee
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
<tr><td><b>Name</b></td><td><code>deployed_ingress_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.deployed_ingress_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the resource in the following format: `organizations/&#123;org&#125;/deployedIngressConfig`. |
| <CopyableCode code="environmentGroups" /> | `array` | List of environment groups in the organization. |
| <CopyableCode code="revisionCreateTime" /> | `string` | Time at which the IngressConfig revision was created. |
| <CopyableCode code="revisionId" /> | `string` | Revision id that defines the ordering on IngressConfig resources. The higher the revision, the more recently the configuration was deployed. |
| <CopyableCode code="uid" /> | `string` | A unique id for the ingress config that will only change if the organization is deleted and recreated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="organizations_get_deployed_ingress_config" /> | `SELECT` | <CopyableCode code="organizationsId" /> |

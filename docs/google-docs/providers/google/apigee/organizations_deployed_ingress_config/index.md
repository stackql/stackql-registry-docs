---
title: organizations_deployed_ingress_config
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations_deployed_ingress_config
  - apigee
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations_deployed_ingress_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.organizations_deployed_ingress_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the resource in the following format: `organizations/{org}/deployedIngressConfig`. |
| `environmentGroups` | `array` | List of environment groups in the organization. |
| `revisionCreateTime` | `string` | Time at which the IngressConfig revision was created. |
| `revisionId` | `string` | Revision id that defines the ordering on IngressConfig resources. The higher the revision, the more recently the configuration was deployed. |
| `uid` | `string` | A unique id for the ingress config that will only change if the organization is deleted and recreated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_getDeployedIngressConfig` | `SELECT` | `organizationsId` |

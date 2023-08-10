---
title: memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - memberships
  - recaptchaenterprise
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recaptchaenterprise.memberships</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name for this membership in the format `projects/&#123;project&#125;/relatedaccountgroups/&#123;relatedaccountgroup&#125;/memberships/&#123;membership&#125;`. |
| `hashedAccountId` | `string` | The unique stable hashed user identifier of the member. The identifier corresponds to a `hashed_account_id` provided in a previous `CreateAssessment` or `AnnotateAssessment` call. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `projectsId, relatedaccountgroupsId` |
| `_list` | `EXEC` | `projectsId, relatedaccountgroupsId` |

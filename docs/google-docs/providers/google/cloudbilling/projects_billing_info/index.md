---
title: projects_billing_info
hide_title: false
hide_table_of_contents: false
keywords:
  - projects_billing_info
  - cloudbilling
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
<tr><td><b>Name</b></td><td><code>projects_billing_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudbilling.projects_billing_info</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name for the `ProjectBillingInfo`; has the form `projects/{project_id}/billingInfo`. For example, the resource name for the billing information for project `tokyo-rain-123` would be `projects/tokyo-rain-123/billingInfo`. This field is read-only. |
| `billingEnabled` | `boolean` | True if the project is associated with an open billing account, to which usage on the project is charged. False if the project is associated with a closed billing account, or no billing account at all, and therefore cannot use paid services. This field is read-only. |
| `projectId` | `string` | The ID of the project that this `ProjectBillingInfo` represents, such as `tokyo-rain-123`. This is a convenience field so that you don't need to parse the `name` field to obtain a project ID. This field is read-only. |
| `billingAccountName` | `string` | The resource name of the billing account associated with the project, if any. For example, `billingAccounts/012345-567890-ABCDEF`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_getBillingInfo` | `SELECT` | `projectsId` |

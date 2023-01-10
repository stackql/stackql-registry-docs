---
title: templates
hide_title: false
hide_table_of_contents: false
keywords:
  - templates
  - tagmanager
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Custom Template display name. |
| `templateId` | `string` | The Custom Template ID uniquely identifies the GTM custom template. |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI |
| `workspaceId` | `string` | GTM Workspace ID. |
| `containerId` | `string` | GTM Container ID. |
| `templateData` | `string` | The custom template in text format. |
| `accountId` | `string` | GTM Account ID. |
| `fingerprint` | `string` | The fingerprint of the GTM Custom Template as computed at storage time. This value is recomputed whenever the template is modified. |
| `galleryReference` | `object` | Represents the link between a custom template and an entry on the Community Template Gallery site. |
| `path` | `string` | GTM Custom Template's API relative path. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_workspaces_templates_get` | `SELECT` | `accountsId, containersId, templatesId, workspacesId` | Gets a GTM Template. |
| `accounts_containers_workspaces_templates_list` | `SELECT` | `accountsId, containersId, workspacesId` | Lists all GTM Templates of a GTM container workspace. |
| `accounts_containers_workspaces_templates_create` | `INSERT` | `accountsId, containersId, workspacesId` | Creates a GTM Custom Template. |
| `accounts_containers_workspaces_templates_delete` | `DELETE` | `accountsId, containersId, templatesId, workspacesId` | Deletes a GTM Template. |
| `accounts_containers_workspaces_templates_revert` | `EXEC` | `accountsId, containersId, templatesId, workspacesId` | Reverts changes to a GTM Template in a GTM Workspace. |
| `accounts_containers_workspaces_templates_update` | `EXEC` | `accountsId, containersId, templatesId, workspacesId` | Updates a GTM Template. |

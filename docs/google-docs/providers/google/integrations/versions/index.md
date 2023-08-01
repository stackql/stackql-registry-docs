---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - integrations
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
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.integrations.versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `integrationTemplateVersions` | `array` | The IntegrationTemplateVersions which match the request. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_integrations_versions_get` | `SELECT` | `integrationsId, locationsId, projectsId, versionsId` | Get a integration in the specified project. |
| `projects_locations_integrations_versions_list` | `SELECT` | `integrationsId, locationsId, projectsId` | Returns the list of all integration versions in the specified project. |
| `projects_locations_products_integrations_versions_get` | `SELECT` | `integrationsId, locationsId, productsId, projectsId, versionsId` | Get a integration in the specified project. |
| `projects_locations_products_integrations_versions_list` | `SELECT` | `integrationsId, locationsId, productsId, projectsId` | Returns the list of all integration versions in the specified project. |
| `projects_locations_products_integrationtemplates_versions_get` | `SELECT` | `integrationtemplatesId, locationsId, productsId, projectsId, versionsId` | Returns an IntegrationTemplateVersion in the specified project. |
| `projects_locations_products_integrationtemplates_versions_list` | `SELECT` | `integrationtemplatesId, locationsId, productsId, projectsId` | Returns the list of all IntegrationTemplateVersions in the specified project. |
| `projects_locations_integrations_versions_create` | `INSERT` | `integrationsId, locationsId, projectsId` | Create a integration with a draft version in the specified project. |
| `projects_locations_products_integrations_versions_create` | `INSERT` | `integrationsId, locationsId, productsId, projectsId` | Create a integration with a draft version in the specified project. |
| `projects_locations_products_integrationtemplates_versions_create` | `INSERT` | `integrationtemplatesId, locationsId, productsId, projectsId` | Creates an IntegrationTemplateVersion. |
| `projects_locations_integrations_versions_delete` | `DELETE` | `integrationsId, locationsId, projectsId, versionsId` | Soft-deletes the integration. Changes the status of the integration to ARCHIVED. If the integration being ARCHIVED is tagged as "HEAD", the tag is removed from this snapshot and set to the previous non-ARCHIVED snapshot. The PUBLISH_REQUESTED, DUE_FOR_DELETION tags are removed too. This RPC throws an exception if the version being deleted is DRAFT, and if the `locked_by` user is not the same as the user performing the Delete. Audit fields updated include last_modified_timestamp, last_modified_by. Any existing lock is released when Deleting a integration. Currently, there is no undelete mechanism. |
| `projects_locations_products_integrations_versions_delete` | `DELETE` | `integrationsId, locationsId, productsId, projectsId, versionsId` | Soft-deletes the integration. Changes the status of the integration to ARCHIVED. If the integration being ARCHIVED is tagged as "HEAD", the tag is removed from this snapshot and set to the previous non-ARCHIVED snapshot. The PUBLISH_REQUESTED, DUE_FOR_DELETION tags are removed too. This RPC throws an exception if the version being deleted is DRAFT, and if the `locked_by` user is not the same as the user performing the Delete. Audit fields updated include last_modified_timestamp, last_modified_by. Any existing lock is released when Deleting a integration. Currently, there is no undelete mechanism. |
| `projects_locations_integrations_versions_download` | `EXEC` | `integrationsId, locationsId, projectsId, versionsId` | Downloads an integration. Retrieves the `IntegrationVersion` for a given `integration_id` and returns the response as a string. |
| `projects_locations_integrations_versions_patch` | `EXEC` | `integrationsId, locationsId, projectsId, versionsId` | Update a integration with a draft version in the specified project. |
| `projects_locations_integrations_versions_publish` | `EXEC` | `integrationsId, locationsId, projectsId, versionsId` | This RPC throws an exception if the integration is in ARCHIVED or ACTIVE state. This RPC throws an exception if the version being published is DRAFT, and if the `locked_by` user is not the same as the user performing the Publish. Audit fields updated include last_published_timestamp, last_published_by, last_modified_timestamp, last_modified_by. Any existing lock is on this integration is released. |
| `projects_locations_integrations_versions_takeover_edit_lock` | `EXEC` | `integrationsId, locationsId, projectsId, versionsId` | Clears the `locked_by` and `locked_at_timestamp`in the DRAFT version of this integration. It then performs the same action as the CreateDraftIntegrationVersion (i.e., copies the DRAFT version of the integration as a SNAPSHOT and then creates a new DRAFT version with the `locked_by` set to the `user_taking_over` and the `locked_at_timestamp` set to the current timestamp). Both the `locked_by` and `user_taking_over` are notified via email about the takeover. This RPC throws an exception if the integration is not in DRAFT status or if the `locked_by` and `locked_at_timestamp` fields are not set.The TakeoverEdit lock is treated the same as an edit of the integration, and hence shares ACLs with edit. Audit fields updated include last_modified_timestamp, last_modified_by. |
| `projects_locations_integrations_versions_unpublish` | `EXEC` | `integrationsId, locationsId, projectsId, versionsId` | Sets the status of the ACTIVE integration to SNAPSHOT with a new tag "PREVIOUSLY_PUBLISHED" after validating it. The "HEAD" and "PUBLISH_REQUESTED" tags do not change. This RPC throws an exception if the version being snapshot is not ACTIVE. Audit fields added include action, action_by, action_timestamp. |
| `projects_locations_integrations_versions_upload` | `EXEC` | `integrationsId, locationsId, projectsId` | Uploads an integration. The content can be a previously downloaded integration. Performs the same function as CreateDraftIntegrationVersion, but accepts input in a string format, which holds the complete representation of the IntegrationVersion content. |
| `projects_locations_products_integrations_versions_download` | `EXEC` | `integrationsId, locationsId, productsId, projectsId, versionsId` | Downloads an integration. Retrieves the `IntegrationVersion` for a given `integration_id` and returns the response as a string. |
| `projects_locations_products_integrations_versions_patch` | `EXEC` | `integrationsId, locationsId, productsId, projectsId, versionsId` | Update a integration with a draft version in the specified project. |
| `projects_locations_products_integrations_versions_publish` | `EXEC` | `integrationsId, locationsId, productsId, projectsId, versionsId` | This RPC throws an exception if the integration is in ARCHIVED or ACTIVE state. This RPC throws an exception if the version being published is DRAFT, and if the `locked_by` user is not the same as the user performing the Publish. Audit fields updated include last_published_timestamp, last_published_by, last_modified_timestamp, last_modified_by. Any existing lock is on this integration is released. |
| `projects_locations_products_integrations_versions_takeover_edit_lock` | `EXEC` | `integrationsId, locationsId, productsId, projectsId, versionsId` | Clears the `locked_by` and `locked_at_timestamp`in the DRAFT version of this integration. It then performs the same action as the CreateDraftIntegrationVersion (i.e., copies the DRAFT version of the integration as a SNAPSHOT and then creates a new DRAFT version with the `locked_by` set to the `user_taking_over` and the `locked_at_timestamp` set to the current timestamp). Both the `locked_by` and `user_taking_over` are notified via email about the takeover. This RPC throws an exception if the integration is not in DRAFT status or if the `locked_by` and `locked_at_timestamp` fields are not set.The TakeoverEdit lock is treated the same as an edit of the integration, and hence shares ACLs with edit. Audit fields updated include last_modified_timestamp, last_modified_by. |
| `projects_locations_products_integrations_versions_unpublish` | `EXEC` | `integrationsId, locationsId, productsId, projectsId, versionsId` | Sets the status of the ACTIVE integration to SNAPSHOT with a new tag "PREVIOUSLY_PUBLISHED" after validating it. The "HEAD" and "PUBLISH_REQUESTED" tags do not change. This RPC throws an exception if the version being snapshot is not ACTIVE. Audit fields added include action, action_by, action_timestamp. |
| `projects_locations_products_integrations_versions_upload` | `EXEC` | `integrationsId, locationsId, productsId, projectsId` | Uploads an integration. The content can be a previously downloaded integration. Performs the same function as CreateDraftIntegrationVersion, but accepts input in a string format, which holds the complete representation of the IntegrationVersion content. |

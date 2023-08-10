---
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
  - essentialcontacts
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
<tr><td><b>Name</b></td><td><code>contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.essentialcontacts.contacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The identifier for the contact. Format: &#123;resource_type&#125;/&#123;resource_id&#125;/contacts/&#123;contact_id&#125; |
| `validationState` | `string` | The validity of the contact. A contact is considered valid if it is the correct recipient for notifications for a particular resource. |
| `email` | `string` | Required. The email address to send notifications to. The email address does not need to be a Google Account. |
| `languageTag` | `string` | Required. The preferred language for notifications, as a ISO 639-1 language code. See [Supported languages](https://cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages) for a list of supported languages. |
| `notificationCategorySubscriptions` | `array` | Required. The categories of notifications that the contact will receive communications for. |
| `validateTime` | `string` | The last time the validation_state was updated, either manually or automatically. A contact is considered stale if its validation state was updated more than 1 year ago. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_contacts_get` | `SELECT` | `contactsId, foldersId` | Gets a single contact. |
| `folders_contacts_list` | `SELECT` | `foldersId` | Lists the contacts that have been set on a resource. |
| `organizations_contacts_get` | `SELECT` | `contactsId, organizationsId` | Gets a single contact. |
| `organizations_contacts_list` | `SELECT` | `organizationsId` | Lists the contacts that have been set on a resource. |
| `projects_contacts_get` | `SELECT` | `contactsId, projectsId` | Gets a single contact. |
| `projects_contacts_list` | `SELECT` | `projectsId` | Lists the contacts that have been set on a resource. |
| `folders_contacts_create` | `INSERT` | `foldersId` | Adds a new contact for a resource. |
| `organizations_contacts_create` | `INSERT` | `organizationsId` | Adds a new contact for a resource. |
| `projects_contacts_create` | `INSERT` | `projectsId` | Adds a new contact for a resource. |
| `folders_contacts_delete` | `DELETE` | `contactsId, foldersId` | Deletes a contact. |
| `organizations_contacts_delete` | `DELETE` | `contactsId, organizationsId` | Deletes a contact. |
| `projects_contacts_delete` | `DELETE` | `contactsId, projectsId` | Deletes a contact. |
| `_folders_contacts_list` | `EXEC` | `foldersId` | Lists the contacts that have been set on a resource. |
| `_organizations_contacts_list` | `EXEC` | `organizationsId` | Lists the contacts that have been set on a resource. |
| `_projects_contacts_list` | `EXEC` | `projectsId` | Lists the contacts that have been set on a resource. |
| `folders_contacts_compute` | `EXEC` | `foldersId` | Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources. |
| `folders_contacts_patch` | `EXEC` | `contactsId, foldersId` | Updates a contact. Note: A contact's email address cannot be changed. |
| `folders_contacts_send_test_message` | `EXEC` | `foldersId` | Allows a contact admin to send a test message to contact to verify that it has been configured correctly. |
| `organizations_contacts_compute` | `EXEC` | `organizationsId` | Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources. |
| `organizations_contacts_patch` | `EXEC` | `contactsId, organizationsId` | Updates a contact. Note: A contact's email address cannot be changed. |
| `organizations_contacts_send_test_message` | `EXEC` | `organizationsId` | Allows a contact admin to send a test message to contact to verify that it has been configured correctly. |
| `projects_contacts_compute` | `EXEC` | `projectsId` | Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources. |
| `projects_contacts_patch` | `EXEC` | `contactsId, projectsId` | Updates a contact. Note: A contact's email address cannot be changed. |
| `projects_contacts_send_test_message` | `EXEC` | `projectsId` | Allows a contact admin to send a test message to contact to verify that it has been configured correctly. |

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
| `nextPageToken` | `string` | If there are more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token` and the rest of the parameters the same as the original request. |
| `contacts` | `array` | The contacts for the specified resource. |
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
| `folders_contacts_compute` | `EXEC` | `foldersId` | Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources. |
| `folders_contacts_patch` | `EXEC` | `contactsId, foldersId` | Updates a contact. Note: A contact's email address cannot be changed. |
| `folders_contacts_send_test_message` | `EXEC` | `foldersId` | Allows a contact admin to send a test message to contact to verify that it has been configured correctly. |
| `organizations_contacts_compute` | `EXEC` | `organizationsId` | Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources. |
| `organizations_contacts_patch` | `EXEC` | `contactsId, organizationsId` | Updates a contact. Note: A contact's email address cannot be changed. |
| `organizations_contacts_send_test_message` | `EXEC` | `organizationsId` | Allows a contact admin to send a test message to contact to verify that it has been configured correctly. |
| `projects_contacts_compute` | `EXEC` | `projectsId` | Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources. |
| `projects_contacts_patch` | `EXEC` | `contactsId, projectsId` | Updates a contact. Note: A contact's email address cannot be changed. |
| `projects_contacts_send_test_message` | `EXEC` | `projectsId` | Allows a contact admin to send a test message to contact to verify that it has been configured correctly. |

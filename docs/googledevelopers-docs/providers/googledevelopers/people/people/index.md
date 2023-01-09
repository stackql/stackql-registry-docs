---
title: people
hide_title: false
hide_table_of_contents: false
keywords:
  - people
  - people
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>people</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.people.people</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `events` | `array` | The person's events. |
| `locales` | `array` | The person's locale preferences. |
| `userDefined` | `array` | The person's user defined data. |
| `residences` | `array` | **DEPRECATED**: (Please use `person.locations` instead) The person's residences. |
| `etag` | `string` | The [HTTP entity tag](https://en.wikipedia.org/wiki/HTTP_ETag) of the resource. Used for web cache validation. |
| `calendarUrls` | `array` | The person's calendar URLs. |
| `photos` | `array` | Output only. The person's photos. |
| `taglines` | `array` | Output only. **DEPRECATED**: No data will be returned The person's taglines. |
| `fileAses` | `array` | The person's file-ases. |
| `resourceName` | `string` | The resource name for the person, assigned by the server. An ASCII string in the form of `people/&#123;person_id&#125;`. |
| `addresses` | `array` | The person's street addresses. |
| `braggingRights` | `array` | **DEPRECATED**: No data will be returned The person's bragging rights. |
| `names` | `array` | The person's names. This field is a singleton for contact sources. |
| `relationshipStatuses` | `array` | Output only. **DEPRECATED**: No data will be returned The person's relationship statuses. |
| `interests` | `array` | The person's interests. |
| `ageRanges` | `array` | Output only. The person's age ranges. |
| `phoneNumbers` | `array` | The person's phone numbers. For `people.connections.list` and `otherContacts.list` the number of phone numbers is limited to 100. If a Person has more phone numbers the entire set can be obtained by calling GetPeople. |
| `occupations` | `array` | The person's occupations. |
| `externalIds` | `array` | The person's external IDs. |
| `organizations` | `array` | The person's past or current organizations. |
| `relations` | `array` | The person's relations. |
| `clientData` | `array` | The person's client data. |
| `relationshipInterests` | `array` | Output only. **DEPRECATED**: No data will be returned The person's relationship interests. |
| `imClients` | `array` | The person's instant messaging clients. |
| `miscKeywords` | `array` | The person's miscellaneous keywords. |
| `birthdays` | `array` | The person's birthdays. This field is a singleton for contact sources. |
| `sipAddresses` | `array` | The person's SIP addresses. |
| `emailAddresses` | `array` | The person's email addresses. For `people.connections.list` and `otherContacts.list` the number of email addresses is limited to 100. If a Person has more email addresses the entire set can be obtained by calling GetPeople. |
| `memberships` | `array` | The person's group memberships. |
| `metadata` | `object` | The metadata about a person. |
| `biographies` | `array` | The person's biographies. This field is a singleton for contact sources. |
| `skills` | `array` | The person's skills. |
| `nicknames` | `array` | The person's nicknames. |
| `genders` | `array` | The person's genders. This field is a singleton for contact sources. |
| `urls` | `array` | The person's associated URLs. |
| `locations` | `array` | The person's locations. |
| `coverPhotos` | `array` | Output only. The person's cover photos. |
| `ageRange` | `string` | Output only. **DEPRECATED** (Please use `person.ageRanges` instead) The person's age range. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `peopleId` | Provides information about a person by specifying a resource name. Use `people/me` to indicate the authenticated user. The request returns a 400 error if 'personFields' is not specified. |
| `batchCreateContacts` | `EXEC` |  | Create a batch of new contacts and return the PersonResponses for the newly Mutate requests for the same user should be sent sequentially to avoid increased latency and failures. |
| `batchDeleteContacts` | `EXEC` |  | Delete a batch of contacts. Any non-contact data will not be deleted. Mutate requests for the same user should be sent sequentially to avoid increased latency and failures. |
| `batchUpdateContacts` | `EXEC` |  | Update a batch of contacts and return a map of resource names to PersonResponses for the updated contacts. Mutate requests for the same user should be sent sequentially to avoid increased latency and failures. |
| `searchContacts` | `EXEC` |  | Provides a list of contacts in the authenticated user's grouped contacts that matches the search query. The query matches on a contact's `names`, `nickNames`, `emailAddresses`, `phoneNumbers`, and `organizations` fields that are from the CONTACT source. **IMPORTANT**: Before searching, clients should send a warmup request with an empty query to update the cache. See https://developers.google.com/people/v1/contacts#search_the_users_contacts |
| `searchDirectoryPeople` | `EXEC` |  | Provides a list of domain profiles and domain contacts in the authenticated user's domain directory that match the search query. |
| `updateContact` | `EXEC` | `peopleId` | Update contact data for an existing contact person. Any non-contact data will not be modified. Any non-contact data in the person to update will be ignored. All fields specified in the `update_mask` will be replaced. The server returns a 400 error if `person.metadata.sources` is not specified for the contact to be updated or if there is no contact source. The server returns a 400 error with reason `"failedPrecondition"` if `person.metadata.sources.etag` is different than the contact's etag, which indicates the contact has changed since its data was read. Clients should get the latest person and merge their updates into the latest person. The server returns a 400 error if `memberships` are being updated and there are no contact group memberships specified on the person. The server returns a 400 error if more than one field is specified on a field that is a singleton for contact sources: * biographies * birthdays * genders * names Mutate requests for the same user should be sent sequentially to avoid increased latency and failures. |
| `updateContactPhoto` | `EXEC` | `peopleId` | Update a contact's photo. Mutate requests for the same user should be sent sequentially to avoid increased latency and failures. |

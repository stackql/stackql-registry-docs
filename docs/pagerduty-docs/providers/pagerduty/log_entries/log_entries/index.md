---
title: log_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - log_entries
  - log_entries
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.log_entries.log_entries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `AnnotateLogEntry__type` | `string` |  |
| `AnnotateLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `AnnotateLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `AnnotateLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `AnnotateLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `AnnotateLogEntry_event_details` | `object` |  |
| `AnnotateLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `AnnotateLogEntry_id` | `string` |  |
| `AnnotateLogEntry_incident` | `object` |  |
| `AnnotateLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `AnnotateLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `AnnotateLogEntry_service` | `object` |  |
| `AnnotateLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `AnnotateLogEntry_teams` | `array` | Will consist of references unless included |
| `AnnotateLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `AssignLogEntry__type` | `string` |  |
| `AssignLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `AssignLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `AssignLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `AssignLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `AssignLogEntry_event_details` | `object` |  |
| `AssignLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `AssignLogEntry_id` | `string` |  |
| `AssignLogEntry_incident` | `object` |  |
| `AssignLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `AssignLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `AssignLogEntry_service` | `object` |  |
| `AssignLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `AssignLogEntry_teams` | `array` | Will consist of references unless included |
| `AssignLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `DelegateLogEntry__type` | `string` |  |
| `DelegateLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `DelegateLogEntry_assignees` | `array` | An array of assigned Users for this log entry |
| `DelegateLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `DelegateLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `DelegateLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `DelegateLogEntry_event_details` | `object` |  |
| `DelegateLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `DelegateLogEntry_id` | `string` |  |
| `DelegateLogEntry_incident` | `object` |  |
| `DelegateLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `DelegateLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `DelegateLogEntry_service` | `object` |  |
| `DelegateLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `DelegateLogEntry_teams` | `array` | Will consist of references unless included |
| `DelegateLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `EscalateLogEntry__type` | `string` |  |
| `EscalateLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `EscalateLogEntry_assignees` | `array` | An array of assigned Users for this log entry |
| `EscalateLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `EscalateLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `EscalateLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `EscalateLogEntry_event_details` | `object` |  |
| `EscalateLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `EscalateLogEntry_id` | `string` |  |
| `EscalateLogEntry_incident` | `object` |  |
| `EscalateLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `EscalateLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `EscalateLogEntry_service` | `object` |  |
| `EscalateLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `EscalateLogEntry_teams` | `array` | Will consist of references unless included |
| `EscalateLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `ExhaustEscalationPathLogEntry__type` | `string` |  |
| `ExhaustEscalationPathLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `ExhaustEscalationPathLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `ExhaustEscalationPathLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `ExhaustEscalationPathLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `ExhaustEscalationPathLogEntry_event_details` | `object` |  |
| `ExhaustEscalationPathLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `ExhaustEscalationPathLogEntry_id` | `string` |  |
| `ExhaustEscalationPathLogEntry_incident` | `object` |  |
| `ExhaustEscalationPathLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `ExhaustEscalationPathLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `ExhaustEscalationPathLogEntry_service` | `object` |  |
| `ExhaustEscalationPathLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `ExhaustEscalationPathLogEntry_teams` | `array` | Will consist of references unless included |
| `ExhaustEscalationPathLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `NotifyLogEntry__type` | `string` |  |
| `NotifyLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `NotifyLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `NotifyLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `NotifyLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `NotifyLogEntry_event_details` | `object` |  |
| `NotifyLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `NotifyLogEntry_id` | `string` |  |
| `NotifyLogEntry_incident` | `object` |  |
| `NotifyLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `NotifyLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `NotifyLogEntry_service` | `object` |  |
| `NotifyLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `NotifyLogEntry_teams` | `array` | Will consist of references unless included |
| `NotifyLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `ReachAckLimitLogEntry__type` | `string` |  |
| `ReachAckLimitLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `ReachAckLimitLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `ReachAckLimitLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `ReachAckLimitLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `ReachAckLimitLogEntry_event_details` | `object` |  |
| `ReachAckLimitLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `ReachAckLimitLogEntry_id` | `string` |  |
| `ReachAckLimitLogEntry_incident` | `object` |  |
| `ReachAckLimitLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `ReachAckLimitLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `ReachAckLimitLogEntry_service` | `object` |  |
| `ReachAckLimitLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `ReachAckLimitLogEntry_teams` | `array` | Will consist of references unless included |
| `ReachAckLimitLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `ReachTriggerLimitLogEntry__type` | `string` |  |
| `ReachTriggerLimitLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `ReachTriggerLimitLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `ReachTriggerLimitLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `ReachTriggerLimitLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `ReachTriggerLimitLogEntry_event_details` | `object` |  |
| `ReachTriggerLimitLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `ReachTriggerLimitLogEntry_id` | `string` |  |
| `ReachTriggerLimitLogEntry_incident` | `object` |  |
| `ReachTriggerLimitLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `ReachTriggerLimitLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `ReachTriggerLimitLogEntry_service` | `object` |  |
| `ReachTriggerLimitLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `ReachTriggerLimitLogEntry_teams` | `array` | Will consist of references unless included |
| `ReachTriggerLimitLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `RepeatEscalationPathLogEntry__type` | `string` |  |
| `RepeatEscalationPathLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `RepeatEscalationPathLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `RepeatEscalationPathLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `RepeatEscalationPathLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `RepeatEscalationPathLogEntry_event_details` | `object` |  |
| `RepeatEscalationPathLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `RepeatEscalationPathLogEntry_id` | `string` |  |
| `RepeatEscalationPathLogEntry_incident` | `object` |  |
| `RepeatEscalationPathLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `RepeatEscalationPathLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `RepeatEscalationPathLogEntry_service` | `object` |  |
| `RepeatEscalationPathLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `RepeatEscalationPathLogEntry_teams` | `array` | Will consist of references unless included |
| `RepeatEscalationPathLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `ResolveLogEntry__type` | `string` |  |
| `ResolveLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `ResolveLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `ResolveLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `ResolveLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `ResolveLogEntry_event_details` | `object` |  |
| `ResolveLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `ResolveLogEntry_id` | `string` |  |
| `ResolveLogEntry_incident` | `object` |  |
| `ResolveLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `ResolveLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `ResolveLogEntry_service` | `object` |  |
| `ResolveLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `ResolveLogEntry_teams` | `array` | Will consist of references unless included |
| `ResolveLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `SnoozeLogEntry__type` | `string` |  |
| `SnoozeLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `SnoozeLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `SnoozeLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `SnoozeLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `SnoozeLogEntry_event_details` | `object` |  |
| `SnoozeLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `SnoozeLogEntry_id` | `string` |  |
| `SnoozeLogEntry_incident` | `object` |  |
| `SnoozeLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `SnoozeLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `SnoozeLogEntry_service` | `object` |  |
| `SnoozeLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `SnoozeLogEntry_teams` | `array` | Will consist of references unless included |
| `SnoozeLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `TriggerLogEntry__type` | `string` |  |
| `TriggerLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `TriggerLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `TriggerLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `TriggerLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `TriggerLogEntry_event_details` | `object` |  |
| `TriggerLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `TriggerLogEntry_id` | `string` |  |
| `TriggerLogEntry_incident` | `object` |  |
| `TriggerLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `TriggerLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `TriggerLogEntry_service` | `object` |  |
| `TriggerLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `TriggerLogEntry_teams` | `array` | Will consist of references unless included |
| `TriggerLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `UnacknowledgeLogEntry__type` | `string` |  |
| `UnacknowledgeLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `UnacknowledgeLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `UnacknowledgeLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `UnacknowledgeLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `UnacknowledgeLogEntry_event_details` | `object` |  |
| `UnacknowledgeLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `UnacknowledgeLogEntry_id` | `string` |  |
| `UnacknowledgeLogEntry_incident` | `object` |  |
| `UnacknowledgeLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `UnacknowledgeLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `UnacknowledgeLogEntry_service` | `object` |  |
| `UnacknowledgeLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `UnacknowledgeLogEntry_teams` | `array` | Will consist of references unless included |
| `UnacknowledgeLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `UrgencyChangeLogEntry__type` | `string` |  |
| `UrgencyChangeLogEntry_agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `UrgencyChangeLogEntry_channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `UrgencyChangeLogEntry_contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `UrgencyChangeLogEntry_created_at` | `string` | Time at which the log entry was created. |
| `UrgencyChangeLogEntry_event_details` | `object` |  |
| `UrgencyChangeLogEntry_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `UrgencyChangeLogEntry_id` | `string` |  |
| `UrgencyChangeLogEntry_incident` | `object` |  |
| `UrgencyChangeLogEntry_note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `UrgencyChangeLogEntry_self` | `string` | the API show URL at which the object is accessible |
| `UrgencyChangeLogEntry_service` | `object` |  |
| `UrgencyChangeLogEntry_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `UrgencyChangeLogEntry_teams` | `array` | Will consist of references unless included |
| `UrgencyChangeLogEntry_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `_created_at` | `string` | Time at which the log entry was created |
| `_type` | `string` |  |
| `acknowledgement_timeout` | `integer` | Duration for which the acknowledgement lasts, in seconds. Services can contain an `acknowledgement_timeout` property, which specifies the length of time acknowledgements should last for. Each time an incident is acknowledged, this timeout is copied into the acknowledgement log entry. This property is optional, as older log entries may not contain it. It may also be `null`, as acknowledgements can be performed on incidents whose services have no `acknowledgement_timeout` set. |
| `agent` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `assignees` | `array` | An array of assigned Users for this log entry |
| `changed_actions` | `array` |  |
| `channel` | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| `contexts` | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| `created_at` | `string` | Time at which the log entry was created. |
| `event_details` | `object` |  |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `incident` | `object` |  |
| `note` | `string` | Optional field containing a note, if one was included with the log entry. |
| `self` | `string` | the API show URL at which the object is accessible |
| `service` | `object` |  |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `teams` | `array` | Will consist of references unless included |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `user` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_log_entry` | `SELECT` | `id` | Get details for a specific incident log entry. This method provides additional information you can use to get at raw event data.<br /><br />A log of all the events that happen to an Incident, and these are exposed as Log Entries.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#log-entries)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| `list_log_entries` | `SELECT` |  | List all of the incident log entries across the entire account.<br /><br />A log of all the events that happen to an Incident, and these are exposed as Log Entries.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#log-entries)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| `_get_log_entry` | `EXEC` | `id` | Get details for a specific incident log entry. This method provides additional information you can use to get at raw event data.<br /><br />A log of all the events that happen to an Incident, and these are exposed as Log Entries.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#log-entries)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| `_list_log_entries` | `EXEC` |  | List all of the incident log entries across the entire account.<br /><br />A log of all the events that happen to an Incident, and these are exposed as Log Entries.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#log-entries)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| `update_log_entry_channel` | `EXEC` | `From, id, data__channel` | Update an existing incident log entry channel.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#log-entries)<br /><br />Scoped OAuth requires: `incidents.write`<br /> |

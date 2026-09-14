# Tool catalog

This catalog contains all 359 operations in the supplied ConnectSecure OpenAPI specification. Put URI IDs in `path_params`, filters/pagination in `query`, required per-call headers in `headers`, and payloads in `body`.

## Auth

- `post_w_authorize` ? Authorize.

## Company

- `get_r_company_asset_windows_compatibility` ? Retrieve asset windows compatibility.
- `get_r_company_companies` ? Retrieve companies.
- `get_r_company_companies_id` ? Retrieve company.
- `post_w_company_companies` ? Create company.
- `patch_w_company_companies` ? Update company.
- `delete_d_company_companies_id` ? Delete company.
- `get_r_company_company_stats` ? Retrieve company stats.
- `get_r_company_company_stats_id` ? Retrieve company stat.
- `get_r_company_jobs_view` ? Retrieve jobs view.
- `get_r_company_jobs_view_id` ? Retrieve job view.
- `get_report_queries_adaudit` ? Retrieve adaudit.
- `get_report_queries_event_tickets` ? Retrieve event tickets.
- `post_w_company_scan` ? Scan Company.

## Agent

- `get_r_company_agents` ? Retrieve agents.
- `get_r_company_agents_id` ? Retrieve agent.
- `post_w_company_reset_agents` ? Migrate Agents.
- `get_r_company_get_uninstall_secret` ? Get uninstall secret token.

## Credentials

- `get_r_company_credentials` ? Retrieve credentials.
- `get_r_company_credentials_id` ? Retrieve credential.
- `post_w_company_credentials` ? Create credential.
- `patch_w_company_credentials` ? Update credential.
- `delete_d_company_credentials_id` ? Delete credential.
- `get_r_company_agent_credentials_mapping` ? Retrieve agent credentials mapping.
- `get_r_company_agent_credentials_mapping_id` ? Retrieve agent credential mapping.
- `post_w_company_agent_credentials_mapping` ? Create agent credential mapping.
- `patch_w_company_agent_credentials_mapping` ? Update agent credential mapping.
- `delete_d_company_agent_credentials_mapping_id` ? Delete agent credential mapping.

## Asset

- `get_r_report_queries_risk_score` ? Retrieve records.
- `post_w_asset_assets` ? Create asset.
- `patch_w_asset_assets` ? Update asset.
- `delete_d_asset_assets_id` ? Delete asset.
- `get_r_report_queries_assets` ? Retrieve assets.
- `get_r_report_queries_asset_stats` ? Retrieve asset stats.
- `get_r_asset_asset_view` ? Retrieve asset view.
- `get_r_asset_asset_view_id` ? Retrieve asset view.
- `get_r_report_queries_lightweight_assets` ? Retrieve records.
- `get_r_report_queries_tags_view` ? Retrieve records.
- `get_r_report_queries_distinct_os` ? Retrieve records.
- `get_r_report_queries_distinct_tags` ? Retrieve records.
- `get_r_report_queries_distinct_asset_name` ? Retrieve records.
- `get_r_report_queries_distinct_asset_ip` ? Retrieve records.
- `get_r_report_queries_distinct_platform` ? Retrieve records.
- `get_r_report_queries_distinct_discovered_protocols` ? Retrieve records.
- `get_r_report_queries_distinct_agents_name` ? Retrieve records.
- `get_r_report_queries_total_asset_count` ? Retrieve records.
- `get_r_report_queries_distinct_software` ? Retrieve records.
- `get_r_report_queries_asset_ports_view` ? Retrieve records.
- `get_r_report_queries_vulnerabilities_count` ? Retrieve records.
- `get_r_report_queries_application_count` ? Retrieve records.
- `get_r_report_queries_compliance_count` ? Retrieve records.
- `get_r_report_queries_ports_count` ? Retrieve records.
- `get_r_report_queries_unconfirmed_open_ports_key_check` ? Retrieve records.
- `get_r_report_queries_asset_software` ? Retrieve records.
- `get_r_report_queries_problems_ssl_for_asset` ? Retrieve records.
- `get_r_report_queries_cert_info_view` ? Retrieve records.
- `get_r_report_queries_get_assets_by_problem` ? Retrieve records.
- `get_r_report_queries_os_pending_patches` ? Retrieve records.
- `get_r_report_queries_remediation_companies` ? Retrieve records.
- `get_r_report_queries_os_pending_patches_companies` ? Retrieve records.
- `get_r_report_queries_ports_view` ? Retrieve records.
- `get_r_report_queries_ports_assets_details` ? Retrieve records.
- `get_r_report_queries_problem_group_summary` ? Retrieve records.
- `get_r_report_queries_problem_group_summary_asset_company_count` ? Retrieve records.
- `get_r_report_queries_problems_remediations_summary` ? Retrieve records.
- `get_r_report_queries_problems_summary` ? Retrieve records.
- `get_r_report_queries_sw_problems_remediations_view` ? Retrieve records.
- `get_r_report_queries_unconfirmed_key_check` ? Retrieve records.
- `get_r_report_queries_suppressed_problems` ? Retrieve records.
- `get_r_report_queries_problems_summary_group_by_companies` ? Retrieve records.
- `get_r_report_queries_problems_summary_tag` ? Retrieve records.
- `get_r_report_queries_problems_summary_asset_details` ? Retrieve records.
- `get_r_report_queries_registry_problems_summary` ? Retrieve records.
- `get_r_report_queries_registry_problems_remediation` ? Retrieve records.
- `get_r_report_queries_registry_problems_company` ? Retrieve records.
- `get_r_report_queries_companies_by_problem_group` ? Retrieve records.
- `get_r_report_queries_companies_by_problem_group_suppressed` ? Retrieve records.
- `get_r_report_queries_remediation_plan_by_company` ? Retrieve records.
- `get_r_report_queries_remediation_plan_include_company` ? Retrieve records.
- `get_r_asset_get_asset_remediation_plan` ? Retrieve records.
- `get_r_report_queries_get_remediation` ? Retrieve records.
- `get_r_report_queries_asset_wise_vulnerabilities` ? Retrieve records.
- `get_r_report_queries_get_remediate_records` ? Retrieve records.
- `get_r_report_queries_remediation_velocity_company` ? Retrieve records.
- `get_r_report_queries_remediation_velocity_application` ? Retrieve records.
- `get_r_report_queries_remediation_velocity_application_asset_details` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_v2` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_patching_asset_details` ? Retrieve records.
- `get_r_report_queries_remediation_plan_asset_details` ? Retrieve records.
- `get_r_report_queries_remediation_plan_asset_epss_details` ? Retrieve records.
- `get_r_report_queries_remediation_plan_asset_details_by_epss` ? Retrieve records.
- `get_r_report_queries_registry_problems_remediation_asset_details` ? Retrieve records.
- `get_r_report_queries_remediate_records` ? Retrieve records.
- `get_r_report_queries_remediate_records_companies` ? Retrieve records.
- `get_r_report_queries_remediate_records_assets` ? Retrieve records.
- `get_r_report_queries_companies_by_application` ? Retrieve records.
- `get_r_report_queries_assets_by_application` ? Retrieve records.
- `get_r_report_queries_assets_by_application_suppressed` ? Retrieve records.
- `get_r_report_queries_companies_by_application_suppressed` ? Retrieve records.
- `get_r_report_queries_vulnerabilities_details` ? Retrieve records.
- `get_r_report_queries_vulnerabilities_details_suppressed` ? Retrieve records.
- `get_r_report_queries_asset_security_report_data` ? Retrieve records.
- `get_r_report_queries_notification_tickets_view` ? Retrieve records.
- `get_report_queries_cron_jobs` ? Retrieve cron jobs.
- `get_report_queries_kernel_modules` ? Retrieve kernel modules.
- `get_report_queries_suid_permissions` ? Retrieve suid permissions.
- `get_report_queries_ufw_firewall_rules` ? Retrieve ufw firewall rules.
- `get_report_queries_selinux_settings` ? Retrieve selinux settings.
- `get_report_queries_asset_iptables_rules` ? Retrieve asset iptables rules.
- `get_report_queries_asset_users` ? Retrieve asset users.
- `get_report_queries_asset_processes_running` ? Retrieve asset processes running.
- `get_report_queries_asset_services` ? Retrieve asset services.
- `get_report_queries_asset_patches_info` ? Retrieve asset patches info.
- `get_report_queries_asset_firewall_rules` ? Retrieve asset firewall rules.
- `get_report_queries_asset_registry_misconfiguration` ? Retrieve asset registry misconfiguration.
- `get_report_queries_asset_open_ports` ? Retrieve asset open ports.
- `get_report_queries_notification_tickets_view` ? Retrieve notification tickets view.
- `get_report_queries_system_events_view` ? Retrieve system events view.
- `get_report_queries_system_events_view_ticketid` ? Retrieve system events view.
- `get_r_report_queries_external_asset_externalscan` ? Retrieve records.
- `get_r_report_queries_external_asset_ports_data` ? Retrieve records.
- `get_r_report_queries_external_asset_ssl_attack` ? Retrieve records.
- `get_r_report_queries_external_asset_vulnerabilities` ? Retrieve records.
- `get_r_report_queries_external_asset_ssl_ciphers` ? Retrieve records.
- `get_r_report_queries_asset_critical_vulnerabilities` ? Retrieve records.
- `get_r_company_get_patch_settings` ? Retrieve records.
- `get_r_report_queries_sw_problems_remediations_view_assetwise` ? Retrieve records.
- `get_r_report_queries_remediation_plan_include_company_days` ? Retrieve records.
- `get_r_report_queries_remediate_records_days` ? Retrieve records.
- `post_w_company_bulk_deprecate` ? Bulk deprecate assets.
- `get_r_report_queries_sw_problems_remediations_view_vul` ? Retrieve records.
- `get_r_report_queries_remediated_registry_solution_plan` ? Retrieve records.
- `get_r_report_queries_get_assets_problem` ? Retrieve records.
- `get_r_report_queries_resolved_remediation` ? Retrieve records.
- `get_r_report_queries_problems_info` ? Retrieve records.
- `get_r_report_queries_problems_summary_global` ? Retrieve records.

## Discovery Settings

- `get_r_company_discovery_settings` ? Retrieve discovery settings.
- `get_r_company_discovery_settings_id` ? Retrieve discovery setting.
- `post_w_company_discovery_settings` ? Create discovery setting.
- `patch_w_company_discovery_settings` ? Update discovery setting.
- `delete_d_company_discovery_settings_id` ? Delete discovery setting.
- `get_r_company_agent_discoverysettings_mapping` ? Retrieve agent discoverysettings mapping.
- `get_r_company_agent_discoverysettings_mapping_id` ? Retrieve agent discoverysetting mapping.
- `post_w_company_agent_discoverysettings_mapping` ? Create agent discoverysetting mapping.
- `patch_w_company_agent_discoverysettings_mapping` ? Update agent discoverysetting mapping.
- `delete_d_company_agent_discoverysettings_mapping_id` ? Delete agent discoverysetting mapping.

## Asset Data

- `get_r_asset_asset_firewall_policy` ? Retrieve asset firewall policy.
- `get_r_asset_asset_firewall_policy_id` ? Retrieve asset firewall policy.
- `get_r_asset_asset_installed_drivers` ? Retrieve asset installed drivers.
- `get_r_asset_asset_installed_drivers_id` ? Retrieve asset installed driver.
- `get_r_asset_asset_interface` ? Retrieve asset interface.
- `get_r_asset_asset_interface_id` ? Retrieve asset interface.
- `get_r_asset_asset_msdt` ? Retrieve asset msdt.
- `get_r_asset_asset_msdt_id` ? Retrieve asset msdt.
- `get_r_asset_asset_ports` ? Retrieve asset ports.
- `get_r_asset_asset_ports_id` ? Retrieve asset port.
- `get_r_asset_asset_security_report_data` ? Retrieve asset security report data.
- `get_r_asset_asset_security_report_data_id` ? Retrieve asset security report datum.
- `get_r_asset_asset_shares` ? Retrieve asset shares.
- `get_r_asset_asset_shares_id` ? Retrieve asset share.
- `get_r_asset_asset_storages` ? Retrieve asset storages.
- `get_r_asset_asset_storages_id` ? Retrieve asset storage.
- `get_r_asset_asset_unqouted_services` ? Retrieve asset unqouted services.
- `get_r_asset_asset_unqouted_services_id` ? Retrieve asset unqouted service.
- `get_r_asset_asset_user_shares` ? Retrieve asset user shares.
- `get_r_asset_asset_user_shares_id` ? Retrieve asset user share.
- `get_r_asset_asset_video_info` ? Retrieve asset video info.
- `get_r_asset_asset_video_info_id` ? Retrieve asset video info.
- `get_r_asset_asset_windows_reboot_required` ? Retrieve asset windows reboot required.
- `get_r_asset_asset_windows_reboot_required_id` ? Retrieve asset window reboot required.
- `get_r_asset_bios_info` ? Retrieve bios info.
- `get_r_asset_bios_info_id` ? Retrieve bio info.
- `get_r_asset_browser_extensions` ? Retrieve browser extensions.
- `get_r_asset_browser_extensions_id` ? Retrieve browser extension.
- `get_r_asset_ciphers_view` ? Retrieve ciphers view.
- `get_r_asset_ciphers_view_id` ? Retrieve cipher view.
- `get_r_asset_windows_protection_status` ? Retrieve windows protection status.
- `get_r_asset_windows_protection_status_id` ? Retrieve window protection status.
- `get_r_report_queries_asset_security_report_data_bulk` ? Retrieve asset security report data.

## Vulnerabilities

- `get_r_asset_suppress_vulnerability` ? Retrieve suppress vulnerability.
- `get_r_asset_suppress_vulnerability_id` ? Retrieve suppres vulnerability.
- `post_w_asset_suppress_vulnerability` ? Create suppres vulnerability.
- `patch_w_asset_suppress_vulnerability` ? Update suppres vulnerability.
- `delete_d_asset_suppress_vulnerability_id` ? Delete suppres vulnerability.
- `get_r_report_queries_application_vulnerabilities_tag` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_suppressed` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_suppressed_tag` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_net` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_net_tag` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_net_suppressed` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_net_suppressed_tag` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_by_product` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_by_product_tag` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_by_product_suppressed` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_by_product_suppressed_tag` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_by_os` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_tag_by_os` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_suppressed_by_os` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_suppressed_tag_by_os` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_by_os_software_details` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_by_os_software_details_suppressed` ? Retrieve records.
- `get_r_report_queries_suppress_vulnerability_problems` ? Retrieve records.
- `get_r_report_queries_suppress_vulnerability_solution` ? Retrieve records.
- `get_r_cve_report` ? Retrieve records.
- `get_r_report_queries_suppress_vulnerability_problems_sid` ? Retrieve records.

## Firewall

- `get_r_asset_firewall_groups` ? Retrieve firewall groups.
- `get_r_asset_firewall_groups_id` ? Retrieve firewall group.
- `get_r_asset_firewall_interfaces` ? Retrieve firewall interfaces.
- `get_r_asset_firewall_interfaces_id` ? Retrieve firewall interface.
- `get_r_asset_firewall_license` ? Retrieve firewall license.
- `get_r_asset_firewall_license_id` ? Retrieve firewall license.
- `get_r_asset_firewall_rules` ? Retrieve firewall rules.
- `get_r_asset_firewall_rules_id` ? Retrieve firewall rule.
- `get_r_asset_firewall_users` ? Retrieve firewall users.
- `get_r_asset_firewall_users_id` ? Retrieve firewall user.
- `get_r_asset_firewall_zones` ? Retrieve firewall zones.
- `get_r_asset_firewall_zones_id` ? Retrieve firewall zone.

## Integration

- `get_r_integration_integration_credentials` ? Retrieve integration credentials.
- `get_r_integration_integration_credentials_id` ? Retrieve integration credential.
- `post_w_integration_integration_credentials` ? Create integration credential.
- `patch_w_integration_integration_credentials` ? Update integration credential.
- `delete_d_integration_integration_credentials_id` ? Delete integration credential.
- `get_r_integration_integration_rules` ? Retrieve integration rules.
- `get_r_integration_integration_rules_id` ? Retrieve integration rule.
- `post_w_integration_integration_rules` ? Create integration rule.
- `patch_w_integration_integration_rules` ? Update integration rule.
- `delete_d_integration_integration_rules_id` ? Delete integration rule.
- `get_r_integration_company_mappings` ? Retrieve company mappings.
- `get_r_integration_company_mappings_id` ? Retrieve company mapping.
- `post_w_integration_company_mappings` ? Create company mapping.
- `patch_w_integration_company_mappings` ? Update company mapping.
- `delete_d_integration_company_mappings_id` ? Delete company mapping.

## Event Set

- `get_r_company_event_set` ? Retrieve event set.
- `get_r_company_event_set_id` ? Retrieve event set.
- `post_w_company_event_set` ? Create event set.
- `patch_w_company_event_set` ? Update event set.
- `delete_d_company_event_set_id` ? Delete event set.

## Ticket Template

- `get_r_company_custom_ticketing_template` ? Retrieve custom ticketing template.
- `get_r_company_custom_ticketing_template_id` ? Retrieve custom ticketing template.
- `post_w_company_custom_ticketing_template` ? Create custom ticketing template.
- `patch_w_company_custom_ticketing_template` ? Update custom ticketing template.
- `delete_d_company_custom_ticketing_template_id` ? Delete custom ticketing template.

## Scheduler

- `get_r_company_scheduler` ? Retrieve scheduler.
- `get_r_company_scheduler_id` ? Retrieve scheduler.
- `post_w_company_scheduler` ? Create scheduler.
- `patch_w_company_scheduler` ? Update scheduler.
- `delete_d_company_scheduler_id` ? Delete scheduler.
- `post_w_company_update_schedule` ? Update schedule.
- `post_w_company_remove_schedule` ? Update schedule.

## Application Baseline

- `get_r_company_application_baseline_rules` ? Retrieve application baseline rules.
- `get_r_company_application_baseline_rules_id` ? Retrieve application baseline rule.
- `post_w_company_application_baseline_rules` ? Create application baseline rule.
- `patch_w_company_application_baseline_rules` ? Update application baseline rule.
- `delete_d_company_application_baseline_rules_id` ? Delete application baseline rule.
- `get_r_company_app_baseline_plan_assets` ? Retrieve app baseline plan assets.
- `get_r_company_app_baseline_plan_assets_id` ? Retrieve app baseline plan asset.
- `get_r_company_app_baseline_plan_company` ? Retrieve app baseline plan company.
- `get_r_company_app_baseline_plan_company_id` ? Retrieve app baseline plan company.
- `get_r_company_app_baseline_plan_global` ? Retrieve app baseline plan global.
- `get_r_company_app_baseline_plan_global_id` ? Retrieve app baseline plan global.

## Attack Surface

- `get_r_company_attack_surface_domain` ? Retrieve attack surface domain.
- `get_r_company_attack_surface_domain_id` ? Retrieve attack surface domain.
- `post_w_company_attack_surface_domain` ? Create attack surface domain.
- `patch_w_company_attack_surface_domain` ? Update attack surface domain.
- `delete_d_company_attack_surface_domain_id` ? Delete attack surface domain.
- `get_r_company_attack_surface_results` ? Retrieve attack surface results.
- `get_r_company_attack_surface_results_id` ? Retrieve attack surface result.

## Backup Software

- `get_r_company_backup_software` ? Retrieve backup software.
- `get_r_company_backup_software_id` ? Retrieve backup software.
- `post_w_company_backup_software` ? Create backup software.
- `patch_w_company_backup_software` ? Update backup software.
- `delete_d_company_backup_software_id` ? Delete backup software.

## EDR

- `get_r_company_edr` ? Retrieve edr.
- `get_r_company_edr_id` ? Retrieve edr.
- `post_w_company_edr` ? Create edr.
- `patch_w_company_edr` ? Update edr.
- `delete_d_company_edr_id` ? Delete edr.

## Tags

- `get_r_company_tag_rules` ? Retrieve tag rules.
- `get_r_company_tag_rules_id` ? Retrieve tag rule.
- `post_w_company_tag_rules` ? Create tag rule.
- `patch_w_company_tag_rules` ? Update tag rule.
- `delete_d_company_tag_rules_id` ? Delete tag rule.
- `get_r_company_tags` ? Retrieve tags.
- `get_r_company_tags_id` ? Retrieve tag.
- `post_w_company_tags` ? Create tag.
- `patch_w_company_tags` ? Update tag.
- `delete_d_company_tags_id` ? Delete tag.

## PII

- `get_r_company_pii_scan_settings` ? Retrieve pii scan settings.
- `get_r_company_pii_scan_settings_id` ? Retrieve pii scan setting.
- `post_w_company_pii_scan_settings` ? Create pii scan setting.
- `patch_w_company_pii_scan_settings` ? Update pii scan setting.
- `delete_d_company_pii_scan_settings_id` ? Delete pii scan setting.

## External Scan

- `get_r_company_custom_profile` ? Retrieve custom profile.
- `get_r_company_custom_profile_id` ? Retrieve custom profile.
- `post_w_company_custom_profile` ? Create custom profile.
- `patch_w_company_custom_profile` ? Update custom profile.
- `delete_d_company_custom_profile_id` ? Delete custom profile.
- `post_w_company_external_scan` ? Scan external endpoint.

## Settings

- `get_r_company_custom_domains` ? Retrieve custom domains.
- `get_r_company_custom_domains_id` ? Retrieve custom domain.
- `post_w_company_custom_domain` ? Custom Domain.

## Compliance Assessment

- `get_r_company_compliance_assessment` ? Retrieve compliance assessment.
- `get_r_company_compliance_assessment_id` ? Retrieve compliance assessment.
- `post_w_company_compliance_assessment` ? Create compliance assessment.
- `patch_w_company_compliance_assessment` ? Update compliance assessment.
- `delete_d_company_compliance_assessment_id` ? Delete compliance assessment.

## Reports

- `get_r_company_report_jobs_view` ? Retrieve report jobs view.
- `get_r_company_report_jobs_view_id` ? Retrieve report job view.
- `get_report_builder_get_report_link` ? Download report.
- `get_report_builder_standard_reports` ? List standard report.
- `post_report_builder_create_report_job` ? Create Report.
- `get_report_builder_get_standard_report_settings` ? Report Settings.
- `post_report_builder_update_standard_report_settings` ? Create Report.
- `get_report_builder_cover_page` ? Report Settings.
- `post_report_builder_cover_page` ? Create Report.
- `get_report_builder_download_default_template` ? Report Settings.
- `post_report_builder_upload_template` ? Report Settings.

## Compliance

- `get_r_compliance_types` ? Retrieve Compliance Types.
- `get_r_report_queries_asset_compliance_report_data` ? Retrieve records.
- `get_r_report_queries_asset_compliance_details` ? Retrieve records.
- `get_r_report_queries_compliance_asset_info` ? Retrieve records.
- `get_r_report_queries_compliance_internal_checks` ? Retrieve records.
- `get_r_report_queries_compliance_maturity` ? Retrieve records.
- `get_r_report_queries_compliance_check_asset_count` ? Retrieve records.
- `get_r_report_queries_compliance_check_company_count` ? Retrieve records.
- `get_r_report_queries_compliance_check_count` ? Retrieve records.
- `get_r_report_queries_compliance_check_count_by_section` ? Retrieve records.

## Jobs

- `get_report_queries_job_details_view` ? Retrieve job details view.
- `get_report_queries_job_details` ? Retrieve job details.

## Active Directory

- `get_report_queries_ad_roles` ? Retrieve ad roles.
- `get_report_queries_ad_user_licenses` ? Retrieve ad user licenses.
- `get_report_queries_azure_licenses` ? Retrieve azure licenses.
- `get_report_queries_azure_ad_logs` ? Retrieve azure ad logs.
- `get_report_queries_azure_secure_score` ? Retrieve azure secure score.
- `get_report_queries_ad_password_policies` ? Retrieve ad password policies.
- `get_report_queries_ad_groups_view` ? Retrieve ad groups view.
- `get_report_queries_ad_ous_view` ? Retrieve ad ous view.
- `get_report_queries_ad_gpos_view` ? Retrieve ad gpos view.
- `get_report_queries_ad_computers_view` ? Retrieve ad computers view.
- `get_report_queries_ad_users_view` ? Retrieve ad users view.
- `get_report_queries_ad_domain_details` ? Retrieve ad domain details.
- `get_report_queries_ad_gpos_details` ? Retrieve ad gpos details.
- `get_report_queries_get_ous_details` ? Retrieve get ous details.
- `get_report_queries_get_groups_details` ? Retrieve get groups details.
- `get_report_queries_ad_group_users` ? Retrieve ad group users.
- `get_report_queries_ad_group_computers` ? Retrieve ad group computers.
- `get_report_queries_get_user_details` ? Retrieve get user details.
- `get_report_queries_get_computer_details` ? Retrieve get computer details.
- `get_report_queries_ad_roles_details` ? Retrieve ad roles details.
- `get_report_queries_ad_roles_member` ? Retrieve ad roles member.
- `get_report_queries_ad_basic_info` ? Retrieve ad basic info.

## Ad Audit

- `get_report_queries_event_stats` ? Retrieve event stats.
- `get_report_queries_user_event_stats` ? Retrieve user event stats.
- `get_report_queries_user_locked_stats` ? Retrieve user locked stats.
- `get_report_queries_user_enabled_stats` ? Retrieve user enabled stats.

## Patch Management

- `post_w_company_patch_now` ? Trigger application/OS patch (now or scheduled).
- `get_r_report_queries_application_vulnerabilities` ? Retrieve records.
- `get_r_report_queries_application_vulnerabilities_os_patch` ? Retrieve records.

## Users

- `get_r_user_get_users` ? Retrieve Users.


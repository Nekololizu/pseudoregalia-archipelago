#pragma once
#include "APClient.hpp"

using namespace RC::Unreal;

namespace Pseudoregalia_AP {
    const char* ip;
    const char* slot_name;
    const char* password;

    GoatManager* goat_manager;
    MapManager* map_manager;

    std::map<std::string, int> obtained_upgrades;


    std::map <std::string, std::vector<APCollectible>> zone_table{
        {"Dungeon", std::vector<APCollectible>{APCollectible("Dungeon", FVector(3500, 4950, -50), 2365810001), APCollectible("Dungeon", FVector(16650, 2600, 2350), 2365810002)}},
        {"Castle", std::vector<APCollectible>{APCollectible("Castle", FVector(5400, 2100, -550), 2365810003)}},
        {"Keep", std::vector<APCollectible>{APCollectible("Dungeon", FVector(-3000, 4900, -400), 2365810004), APCollectible("Dungeon", FVector(10050, 1800, 85), 2365810005)}},
        {"Theatre", std::vector<APCollectible>{APCollectible("Theatre", FVector(8500, 7850, -1400), 2365810005)}},
        {"Underbelly", std::vector<APCollectible>{APCollectible("Underbelly", FVector(-5400, 6650, 6750), 2365810006)}},
        {"Bailey", std::vector<APCollectible>{APCollectible("Bailey", FVector(-1100, 10850, 150), 2365810007)}},
        {"Tower", std::vector<APCollectible>{APCollectible("Tower", FVector(13350, 5250, 4150), 2365810008)}},
    };

    APClient::APClient() {
        // probably take in slot name and ip here instead
        map_manager = new MapManager();
        goat_manager = new GoatManager();
    }

    void APClient::Connect(const char* new_ip, const char* new_slot_name, const char* new_password) {
        ip = new_ip;
        slot_name = new_slot_name;
        password = new_password;
        Initialize();
    }

    void APClient::Initialize() {
        AP_Init(ip, "Pseudoregalia", slot_name, password);

        // These are static but might fuck with members of APClient so... I might need to refactor this entire thing
        AP_SetItemClearCallback(&ClearItems);
        AP_SetItemRecvCallback(&ReceiveItem);
        AP_SetLocationCheckedCallback(&CheckLocation);

        AP_Start();
    }

    void APClient::ClearItems() {
    }

    void APClient::ReceiveItem(int64_t, bool) {

    }

    void APClient::CheckLocation(int64_t) {
    }

    void APClient::SendCheck(int id) {
        AP_SendItem(id);
    }

    void APClient::OnMapLoad() {
        // TODO: figure out a way to identify which map has been loaded, and pick the right one
        map_manager->SpawnCollectibles(zone_table["Dungeon"]);
    }
}